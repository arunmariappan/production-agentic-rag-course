import asyncio
import logging
from typing import List

import httpx
from src.schemas.embeddings.jina import JinaEmbeddingRequest, JinaEmbeddingResponse

logger = logging.getLogger(__name__)


class JinaEmbeddingsClient:
    """Client for Jina AI embeddings API.

    Uses Jina embeddings v3 model with 1024 dimensions optimized for retrieval.
    Documentation: https://jina.ai/embeddings
    """

    def __init__(self, api_key: str, base_url: str = "https://api.jina.ai/v1"):
        """Initialize Jina embeddings client.

        :param api_key: Jina API key
        :param base_url: API base URL
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self.client = httpx.AsyncClient(timeout=30.0)
        logger.info("Jina embeddings client initialized")

    async def _post_embeddings(self, request_data: JinaEmbeddingRequest, max_retries: int = 6) -> httpx.Response:
        """POST to the embeddings endpoint, waiting and retrying when rate limited (HTTP 429).

        The free Jina tier limits tokens per minute, so indexing several papers in a row hits 429s.
        Waits for the Retry-After header if present, otherwise backs off 5s, 10s, 20s, ... (capped at 60s).

        :param request_data: Embedding request payload
        :param max_retries: Maximum retries after a 429 response
        :returns: Successful response
        :raises httpx.HTTPStatusError: On non-429 errors, or 429 after max_retries
        """
        attempt = 0
        while True:
            response = await self.client.post(f"{self.base_url}/embeddings", headers=self.headers, json=request_data.model_dump())
            if response.status_code != 429 or attempt >= max_retries:
                response.raise_for_status()
                return response

            retry_after = response.headers.get("Retry-After", "")
            delay = float(retry_after) if retry_after.isdigit() else min(5 * 2**attempt, 60)
            attempt += 1
            logger.warning(f"Jina rate limit hit (429), retrying in {delay:.0f}s (retry {attempt}/{max_retries})")
            await asyncio.sleep(delay)

    async def embed_passages(self, texts: List[str], batch_size: int = 100) -> List[List[float]]:
        """Embed text passages for indexing.

        :param texts: List of text passages to embed
        :param batch_size: Number of texts to process in each API call
        :returns: List of embedding vectors
        """
        embeddings = []

        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]

            request_data = JinaEmbeddingRequest(
                model="jina-embeddings-v3", task="retrieval.passage", dimensions=1024, input=batch
            )

            try:
                response = await self._post_embeddings(request_data)

                result = JinaEmbeddingResponse(**response.json())
                batch_embeddings = [item["embedding"] for item in result.data]
                embeddings.extend(batch_embeddings)

                logger.debug(f"Embedded batch of {len(batch)} passages")

            except httpx.HTTPError as e:
                logger.error(f"Error embedding passages: {e}")
                raise
            except Exception as e:
                logger.error(f"Unexpected error in embed_passages: {e}")
                raise

        logger.info(f"Successfully embedded {len(texts)} passages")
        return embeddings

    async def embed_query(self, query: str) -> List[float]:
        """Embed a search query.

        :param query: Query text to embed
        :returns: Embedding vector for the query
        """
        request_data = JinaEmbeddingRequest(model="jina-embeddings-v3", task="retrieval.query", dimensions=1024, input=[query])

        try:
            # Few retries: queries are interactive and callers can fall back to BM25
            response = await self._post_embeddings(request_data, max_retries=2)

            result = JinaEmbeddingResponse(**response.json())
            embedding = result.data[0]["embedding"]

            logger.debug(f"Embedded query: '{query[:50]}...'")
            return embedding

        except httpx.HTTPError as e:
            logger.error(f"Error embedding query: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in embed_query: {e}")
            raise

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
