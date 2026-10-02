# The Mother of AI Project
## Phase 1 RAG Systems: arXiv Paper Curator

<div align="center">
  <h3>A Learner-Focused Journey into Production RAG Systems</h3>
  <p>Learn to build modern AI systems from the ground up through hands-on implementation</p>
  <p>Master the most in-demand AI engineering skills: <strong>RAG (Retrieval-Augmented Generation)</strong></p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/FastAPI-0.115+-green.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/OpenSearch-2.19-orange.svg" alt="OpenSearch">
  <img src="https://img.shields.io/badge/Docker-Compose-blue.svg" alt="Docker">
  <img src="https://img.shields.io/badge/Status-Week%207%20Advanced%20Features-brightgreen.svg" alt="Status">
</p>

</br>

<p align="center">
  <a href="#-about-this-course">
    <img src="static/mother_of_ai_project_rag_architecture.gif" alt="RAG Architecture" width="700">
  </a>
</p>

## 📖 About This Course

This is a **learner-focused project** where you'll build a complete research assistant system that automatically fetches academic papers, understands their content, and answers your research questions using advanced RAG techniques.

**The arXiv Paper Curator** will teach you to build a **production-grade RAG system using industry best practices**. Unlike tutorials that jump straight to vector search, we follow the **professional path**: master keyword search foundations first, then enhance with vectors for hybrid retrieval.

> **🎯 The Professional Difference:** We build RAG systems the way successful companies do - solid search foundations enhanced with AI, not AI-first approaches that ignore search fundamentals.

By the end of this course, you'll have your own AI research assistant and the deep technical skills to build production RAG systems for any domain.

### **🎓 What You'll Build**

- **Week 1:** Complete infrastructure with Docker, FastAPI, PostgreSQL, OpenSearch, and Airflow
- **Week 2:** Automated data pipeline fetching and parsing academic papers from arXiv  
- **Week 3:** Production BM25 keyword search with filtering and relevance scoring
- **Week 4:** Intelligent chunking + hybrid search combining keywords with semantic understanding
- **Week 5:** Complete RAG pipeline with local LLM, streaming responses, and Gradio interface
- **Week 6:** Production monitoring with Langfuse tracing and Redis caching for optimized performance
- **Week 7:** **Agentic RAG with LangGraph and Telegram Bot for mobile access**

---

## 🏗️ System Architecture Evolution

### Week 7: Agentic RAG & Telegram Bot Integration
<div align="center">
  <img src="static/week7_telegram_and_agentic_ai.png" alt="Week 7 Telegram and Agentic AI Architecture" width="800">
  <p><em>Complete Week 7 architecture showing Telegram bot integration with the agentic RAG system</em></p>
</div>

### LangGraph Agentic RAG Workflow
<div align="center">
  <img src="static/langgraph-mermaid.png" alt="LangGraph Agentic RAG Flow" width="800">
  <p><em>Detailed LangGraph workflow showing decision nodes, document grading, and adaptive retrieval</em></p>
</div>


**Week 7 Code walkthrough + blog:** [Agentic RAG with LangGraph and Telegram](https://jamwithai.substack.com/p/agentic-rag-with-langgraph-and-telegram) 

**Key Innovations in Week 7:**
- **Intelligent Decision-Making**: Agents evaluate and adapt retrieval strategies
- **Document Grading**: Automatic relevance assessment with semantic evaluation
- **Query Rewriting**: Adaptive query refinement when results are insufficient
- **Guardrails**: Out-of-domain detection prevents hallucination
- **Mobile Access**: Telegram bot for conversational AI on any device
- **Transparency**: Full reasoning step tracking for debugging and trust

---

## 🚀 Quick Start

### **📋 Prerequisites**
- **Docker Desktop** (with Docker Compose)  
- **Python 3.12** (the project requires `>=3.12,<3.13`)
- **UV Package Manager** ([Install Guide](https://docs.astral.sh/uv/getting-started/installation/))
- **8GB+ RAM** and **20GB+ free disk space**

### **⚡ Get Started**

```bash
# 1. Clone and setup
git clone <repository-url>
cd production-agentic-rag-course

# 2. Configure environment (IMPORTANT!)
cp .env.example .env
# The .env file contains all necessary configuration for OpenSearch,
# arXiv API, and service connections. Most defaults work out of the box.
# Then edit .env:
#   - JINA_API_KEY: free Jina AI key (required for hybrid search and indexing)
#   - LANGFUSE__PUBLIC_KEY / LANGFUSE__SECRET_KEY: optional tracing keys (see Configuration)
#   - LANGFUSE_ENCRYPTION_KEY: replace the placeholder with `openssl rand -hex 32`
#   - TELEGRAM__ENABLED=false unless you have a bot token (see Week 7)

# 3. Install dependencies
uv sync

# 4. Start all services
docker compose up --build -d

# 5. Pull the default LLM into the Ollama container (one-time)
docker exec rag-ollama ollama pull llama3.2:1b

# 6. Verify everything works
curl http://localhost:8000/api/v1/health
```

### **📚 Weekly Learning Path**

| Week | Topic | Blog Post | Code Release |
|------|-------|-----------|--------------|
| **Week 0** | The Mother of AI project - 6 phases | [The Mother of AI project](https://jamwithai.substack.com/p/the-mother-of-ai-project) | - |
| **Week 1** | Infrastructure Foundation | [The Infrastructure That Powers RAG Systems](https://jamwithai.substack.com/p/the-infrastructure-that-powers-rag) | [week1.0](https://github.com/jamwithai/arxiv-paper-curator/releases/tag/week1.0) |
| **Week 2** | Data Ingestion Pipeline | [Building Data Ingestion Pipelines for RAG](https://jamwithai.substack.com/p/bringing-your-rag-system-to-life) | [week2.0](https://github.com/jamwithai/arxiv-paper-curator/releases/tag/week2.0) |
| **Week 3** | OpenSearch ingestion & BM25 retrieval | [The Search Foundation Every RAG System Needs](https://jamwithai.substack.com/p/the-search-foundation-every-rag-system) | [week3.0](https://github.com/jamwithai/arxiv-paper-curator/releases/tag/week3.0) |
| **Week 4** | **Chunking & Hybrid Search** | [The Chunking Strategy That Makes Hybrid Search Work](https://jamwithai.substack.com/p/chunking-strategies-and-hybrid-rag) | [week4.0](https://github.com/jamwithai/arxiv-paper-curator/releases/tag/week4.0) |
| **Week 5** | **Complete RAG system** | [The Complete RAG System](https://jamwithai.substack.com/p/the-complete-rag-system) | [week5.0](https://github.com/jamwithai/arxiv-paper-curator/releases/tag/week5.0) |
| **Week 6** | **Production monitoring & caching** | [Production-ready RAG: Monitoring & Caching](https://jamwithai.substack.com/p/production-ready-rag-monitoring-and) | [week6.0](https://github.com/jamwithai/arxiv-paper-curator/releases/tag/week6.0) |
| **Week 7** | **Agentic RAG & Telegram Bot** | [Agentic RAG with LangGraph and Telegram](https://jamwithai.substack.com/p/agentic-rag-with-langgraph-and-telegram) | [week7.0](https://github.com/jamwithai/arxiv-paper-curator/releases/tag/week7.0) |

**📥 Clone a specific week's release:**
```bash
# Clone a specific week's code
git clone --branch <WEEK_TAG> https://github.com/jamwithai/arxiv-paper-curator
cd arxiv-paper-curator
uv sync
docker compose down -v
docker compose up --build -d

# Replace <WEEK_TAG> with: week1.0, week2.0, etc.
```

### **📊 Access Your Services**

| Service | URL | Purpose |
|---------|-----|---------|
| **API Documentation** | http://localhost:8000/docs | Interactive API testing |
| **Gradio RAG Interface** | http://localhost:7861 | User-friendly chat interface (start it with `uv run python gradio_launcher.py`) |
| **Langfuse Dashboard** | http://localhost:3001 | RAG pipeline monitoring & tracing |
| **Airflow Dashboard** | http://localhost:8080 | Workflow management |
| **OpenSearch Dashboards** | http://localhost:5601 | Hybrid search engine UI |

#### **NOTE**: Default logins: Airflow `admin` / `admin` (created by `airflow/entrypoint.sh`); Langfuse `admin@example.com` / `admin123` (set in `compose.yml`). Change both outside local development.
---

## 📚 Week 1: Infrastructure Foundation ✅

**Start here!** Master the infrastructure that powers modern RAG systems.

### **🎯 Learning Objectives**
- Complete infrastructure setup with Docker Compose
- FastAPI development with automatic documentation and health checks
- PostgreSQL database configuration and management
- OpenSearch hybrid search engine setup
- Ollama local LLM service configuration
- Service orchestration and health monitoring
- Professional development environment with code quality tools

### **🏗️ Architecture Overview**

<p align="center">
  <img src="static/week1_infra_setup.png" alt="Week 1 Infrastructure Setup" width="800">
</p>

**Infrastructure Components:**
- **FastAPI**: REST endpoints with async support (Port 8000)  
- **PostgreSQL 16**: Paper metadata storage (Port 5432)
- **OpenSearch 2.19**: Search engine with dashboards (Ports 9200, 5601)
- **Apache Airflow 2.10**: Workflow orchestration (Port 8080)
- **Ollama**: Local LLM server (Port 11434)

### **📓 Setup Guide**

```bash
# Launch the Week 1 notebook
uv run jupyter notebook notebooks/week1/week1_setup.ipynb
```

**Completion Guide:** Follow the [Week 1 notebook](notebooks/week1/week1_setup.ipynb) for hands-on setup and verification steps.

### **📖 Deep Dive**
**Blog Post:** [The Infrastructure That Powers RAG Systems](https://jamwithai.substack.com/p/the-infrastructure-that-powers-rag) - Detailed walkthrough and production insights

---

## 📚 Week 2: Data Ingestion Pipeline ✅

**Building on Week 1 infrastructure:** Learn to fetch, process, and store academic papers automatically.

### **🎯 Learning Objectives**
- arXiv API integration with rate limiting and retry logic
- Scientific PDF parsing using Docling
- Automated data ingestion pipelines with Apache Airflow
- Metadata extraction and storage workflows
- Complete paper processing from API to database

### **🏗️ Architecture Overview**

<p align="center">
  <img src="static/week2_data_ingestion_flow.png" alt="Week 2 Data Ingestion Architecture" width="800">
</p>

**Data Pipeline Components:**
- **MetadataFetcher**: 🎯 Main orchestrator coordinating the entire pipeline
- **ArxivClient**: Rate-limited paper fetching with retry logic
- **PDFParserService**: Docling-powered scientific document processing  
- **Airflow DAGs**: `arxiv_paper_ingestion` runs Monday–Friday at 06:00 UTC (`airflow/dags/`)
- **PostgreSQL Storage**: Structured paper metadata and content (tables are created automatically on startup)

### **📓 Implementation Guide**

```bash
# Launch the Week 2 notebook  
uv run jupyter notebook notebooks/week2/week2_arxiv_integration.ipynb
```

**Completion Guide:** Follow the [Week 2 notebook](notebooks/week2/week2_arxiv_integration.ipynb) for hands-on implementation and verification steps.

### **📖 Deep Dive**
**Blog Post:** [Building Data Ingestion Pipelines for RAG](https://jamwithai.substack.com/p/bringing-your-rag-system-to-life) - arXiv API integration and PDF processing

---

## 📚 Week 3: Keyword Search First - The Critical Foundation

**Building on Weeks 1-2 foundation:** Implement the keyword search foundation that professional RAG systems rely on.

### **🎯 Learning Objectives**
- Why keyword search is essential for RAG systems (foundation first approach)
- OpenSearch index management, mappings, and search optimization
- BM25 algorithm and the math behind effective keyword search
- Query DSL for building complex search queries with filters and boosting
- Search analytics for measuring relevance and performance
- Production patterns used by real companies

### **🏗️ Architecture Overview**

<p align="center">
  <img src="static/week3_opensearch_flow.png" alt="Week 3 OpenSearch Flow Architecture" width="800">
</p>

**Search Infrastructure Components:**
- **OpenSearch Service**: `src/services/opensearch/` - Professional search service implementation (BM25 queries built in `query_builder.py`)
- **Search API**: `src/routers/hybrid_search.py` - BM25 keyword search via `POST /api/v1/hybrid-search/` with `"use_hybrid": false` (the Week 3 search endpoint was folded into this unified endpoint in Week 4)
- **Learning Materials**: `notebooks/week3/` - Complete OpenSearch integration guide
- **Quality Metrics**: Precision, recall, and relevance scoring

### **📓 Setup Guide**

```bash
# Launch the Week 3 notebook
uv run jupyter notebook notebooks/week3/week3_opensearch.ipynb
```

**Completion Guide:** Follow the [Week 3 notebook](notebooks/week3/week3_opensearch.ipynb) for hands-on OpenSearch setup and BM25 search implementation.

### **📖 Deep Dive**
**Blog Post:** [The Search Foundation Every RAG System Needs](https://jamwithai.substack.com/p/the-search-foundation-every-rag-system) - Complete BM25 implementation with OpenSearch

---

## 📚 Week 4: Chunking & Hybrid Search - The Semantic Layer

**Building on Week 3 foundation:** Add the semantic layer that makes search truly intelligent.

### **🎯 Learning Objectives**
- Section-based chunking with intelligent document segmentation
- Production embeddings with Jina AI integration and fallback strategies
- Hybrid search mastery using RRF fusion for keyword + semantic retrieval
- Unified API design with single endpoint supporting multiple search modes
- Performance analysis and trade-offs between search approaches

### **🏗️ Architecture Overview**

<p align="center">
  <img src="static/week4_hybrid_opensearch.png" alt="Week 4 Hybrid Search Architecture" width="800">
</p>

**Hybrid Search Infrastructure Components:**
- **Text Chunker**: `src/services/indexing/text_chunker.py` - Section-aware chunking with overlap strategies
- **Embeddings Service**: `src/services/embeddings/` - Production embedding pipeline with Jina AI (`jina-embeddings-v3`, 1024 dimensions)
- **Hybrid Indexer**: `src/services/indexing/hybrid_indexer.py` - Chunks, embeds, and bulk-indexes papers into the `arxiv-papers-chunks` index; run by the Airflow DAG's `index_papers_hybrid` task
- **Hybrid Search API**: `src/routers/hybrid_search.py` - Unified search API supporting all modes (RRF fusion via an OpenSearch search pipeline, falls back to BM25 if embedding fails)
- **Learning Materials**: `notebooks/week4/` - Complete hybrid search implementation guide

### **📓 Setup Guide**

```bash
# Launch the Week 4 notebook
uv run jupyter notebook notebooks/week4/week4_hybrid_search.ipynb
```

**Completion Guide:** Follow the [Week 4 notebook](notebooks/week4/week4_hybrid_search.ipynb) for hands-on implementation and verification steps.

### **📖 Deep Dive**
**Blog Post:** [The Chunking Strategy That Makes Hybrid Search Work](https://jamwithai.substack.com/p/chunking-strategies-and-hybrid-rag) - Production chunking and RRF fusion implementation

---

## 📚 Week 5: Complete RAG Pipeline with LLM Integration

**Building on Week 4 hybrid search:** Add the LLM layer that turns search into intelligent conversation.

### **🎯 Learning Objectives**
- Local LLM integration with Ollama for complete data privacy
- Performance optimization with 80% prompt reduction (6x speed improvement)
- Streaming implementation using Server-Sent Events for real-time responses
- Dual API design with standard and streaming endpoints
- Interactive Gradio interface with advanced parameter controls

### **🏗️ Architecture Overview**

<p align="center">
  <img src="static/week5_complete_rag.png" alt="Week 5 Complete RAG System Architecture" width="900">
</p>

**Complete RAG Infrastructure Components:**
- **RAG Endpoints**: `src/routers/ask.py` - Dual endpoints (`/api/v1/ask` + `/api/v1/stream`)
- **Ollama Service**: `src/services/ollama/` - LLM client with optimized prompts
- **System Prompt**: `src/services/ollama/prompts/rag_system.txt` - Optimized for academic papers
- **Gradio Interface**: `src/gradio_app.py` - Interactive web UI with streaming support
- **Launcher Script**: `gradio_launcher.py` - Easy-launch script (runs on port 7861)

### **📓 Setup Guide**

```bash
# Launch the Week 5 notebook
uv run jupyter notebook notebooks/week5/week5_complete_rag_system.ipynb

# Launch Gradio interface
uv run python gradio_launcher.py
# Open http://localhost:7861
```

**Completion Guide:** Follow the [Week 5 notebook](notebooks/week5/week5_complete_rag_system.ipynb) for hands-on LLM integration and RAG pipeline implementation.

### **📖 Deep Dive**
**Blog Post:** [The Complete RAG System](https://jamwithai.substack.com/p/the-complete-rag-system) - Complete RAG system with local LLM integration and optimization techniques

---

## 📚 Week 6: Production Monitoring and Caching

**Building on Week 5 complete RAG system:** Add observability, performance optimization, and production-grade monitoring.

### **🎯 Learning Objectives**
- Langfuse integration for end-to-end RAG pipeline tracing
- Redis caching strategy with intelligent cache keys and TTL management
- Performance monitoring with real-time dashboards for latency and costs
- Production patterns for observability and optimization
- Cost analysis and LLM usage optimization (150-400x speedup with caching)

### **🏗️ Architecture Overview**

<p align="center">
  <img src="static/week6_monitoring_and_caching.png" alt="Week 6 Monitoring & Caching Architecture" width="900">
</p>

**Production Infrastructure Components:**
- **Langfuse Service**: `src/services/langfuse/` - Complete tracing integration with RAG-specific metrics
- **Cache Service**: `src/services/cache/` - Redis client with exact-match caching and graceful fallback
- **Updated Endpoints**: `src/routers/ask.py` - Integrated tracing and caching middleware
- **Docker Config**: `compose.yml` - Added Redis service and a self-hosted Langfuse v3 stack (web, worker, Postgres, ClickHouse, Redis, MinIO)
- **Learning Materials**: `notebooks/week6/` - Complete monitoring and caching implementation guide

### **📓 Setup Guide**

```bash
# Launch the Week 6 notebook
uv run jupyter notebook notebooks/week6/week6_cache_testing.ipynb
```

**Completion Guide:** Follow the [Week 6 notebook](notebooks/week6/week6_cache_testing.ipynb) for hands-on Langfuse tracing and Redis caching implementation.

### **📖 Deep Dive**
**Blog Post:** [Production-ready RAG: Monitoring & Caching](https://jamwithai.substack.com/p/production-ready-rag-monitoring-and) - Production-ready RAG with monitoring and caching

---

## 📚 Week 7: Agentic RAG with LangGraph and Telegram Bot

**Building on Week 6 production system:** Add intelligent reasoning, multi-step decision-making, and Telegram bot integration for mobile-first AI interactions.

### **🎯 Learning Objectives**
- LangGraph workflows for state-based agent orchestration with decision nodes
- Guardrail implementation for query validation and domain boundary detection
- Document grading with semantic relevance evaluation
- Query rewriting for automatic query refinement and better retrieval
- Adaptive retrieval with multi-attempt retrieval and intelligent fallback
- Telegram bot integration with async operations and error handling
- Reasoning transparency by exposing agent decision-making process

### **🏗️ Architecture Overview**

<p align="center">
  <img src="static/week7_telegram_and_agentic_ai.png" alt="Week 7 Agentic RAG & Telegram Architecture" width="900">
</p>

**Agentic RAG Infrastructure Components:**
- **Agent Nodes**: `src/services/agents/nodes/` - Guardrail, out-of-scope, retrieve, grade, rewrite, and generate nodes
- **Workflow Orchestration**: `src/services/agents/agentic_rag.py` - LangGraph workflow coordination
- **Retriever Tool**: `src/services/agents/tools.py` - `retrieve_papers` tool wrapping hybrid search
- **Telegram Bot**: `src/services/telegram/` - Command handlers and message processing
- **Agentic Endpoints**: `src/routers/agentic_ask.py` - `POST /api/v1/ask-agentic` (answer + reasoning steps + Langfuse `trace_id`) and `POST /api/v1/feedback` (score a response by `trace_id`)
- **Learning Materials**: `notebooks/week7/` - Week 7 learning materials and examples

**Agent workflow:** `guardrail` scores whether the question is in scope (CS/AI/ML, threshold 60/100). Out-of-scope questions get a polite refusal; in-scope ones go to `retrieve` → `grade_documents`. Relevant documents go to `generate_answer`; otherwise `rewrite_query` refines the question and retrieval is retried (up to 2 attempts).

### **📓 Setup Guide**

```bash
# Launch the Week 7 notebook
uv run jupyter notebook notebooks/week7/week7_agentic_rag.ipynb
```

**Telegram bot:** create a bot with [@BotFather](https://t.me/BotFather), set `TELEGRAM__ENABLED=true` and `TELEGRAM__BOT_TOKEN=<token>` in `.env`, then restart the API (`docker compose up --build -d api`). The bot starts with the API and uses polling, so no webhook is needed. Send it any question, or use `/start`, `/help`, or `/search <keywords>`.

**Completion Guide:** Follow the [Week 7 notebook](notebooks/week7/week7_agentic_rag.ipynb) for hands-on LangGraph agentic RAG and Telegram bot implementation.

### **📖 Deep Dive**
**Blog Post:** [Agentic RAG with LangGraph and Telegram](https://jamwithai.substack.com/p/agentic-rag-with-langgraph-and-telegram) - Building intelligent agents with decision-making, adaptive retrieval, and mobile access

---

## ⚙️ Configuration

**Setup:**
```bash
cp .env.example .env
# Edit .env for your environment
```

**Key Variables:**
- `JINA_API_KEY` - Required for Week 4+ (hybrid search with embeddings)
- `OLLAMA_MODEL` - LLM used for generation (default `llama3.2:1b`; pull it into the Ollama container first)
- `TELEGRAM__ENABLED` & `TELEGRAM__BOT_TOKEN` - Required for Week 7 (Telegram bot integration)
- `LANGFUSE__PUBLIC_KEY` & `LANGFUSE__SECRET_KEY` - Optional for Week 6 (monitoring). Log in to Langfuse at http://localhost:3001, create API keys for a project, and paste them here.

**How settings are read** ([src/config.py](src/config.py)):
- Grouped settings use a **double-underscore** prefix: `ARXIV__`, `PDF_PARSER__`, `CHUNKING__`, `OPENSEARCH__`, `LANGFUSE__`, `REDIS__`, `TELEGRAM__` (for example, `CHUNKING__CHUNK_SIZE=600`).
- `.env.example` also contains single-underscore `LANGFUSE_*` entries (`LANGFUSE_PUBLIC_KEY`, `LANGFUSE_HOST`, ...). The API does **not** read those for tracing. Use the `LANGFUSE__*` names above. Keep the `LANGFUSE_NEXTAUTH_SECRET`, `LANGFUSE_SALT`, `LANGFUSE_ENCRYPTION_KEY`, and other Langfuse server variables, because `compose.yml` uses them to run Langfuse itself.
- Hostnames in `.env` are Docker service names (`postgres`, `opensearch`, `ollama`, `redis`). To run the API or notebooks directly on your machine, point them at `localhost` instead.

**Complete Configuration:** See [.env.example](.env.example) for all available options and detailed documentation.

---

## 🔧 Reference & Development Guide

### **🛠️ Technology Stack**

| Service | Purpose | Status |
|---------|---------|--------|
| **FastAPI** | REST API with automatic docs | ✅ Ready |
| **PostgreSQL 16** | Paper metadata and content storage | ✅ Ready |
| **OpenSearch 2.19** | Hybrid search engine (BM25 + Vector) | ✅ Ready |
| **Apache Airflow 2.10** | Workflow automation | ✅ Ready |
| **Docling** | Scientific PDF parsing (Week 2) | ✅ Ready |
| **Jina AI** | Embedding generation (Week 4) | ✅ Ready |
| **Ollama** | Local LLM serving (Week 5) | ✅ Ready |
| **Gradio** | Web chat interface (Week 5) | ✅ Ready |
| **Redis** | High-performance caching (Week 6) | ✅ Ready |
| **Langfuse v3** | RAG pipeline observability (Week 6) | ✅ Ready |
| **LangGraph** | Agentic RAG workflow (Week 7) | ✅ Ready |
| **Telegram Bot API** | Mobile chat access (Week 7) | ✅ Ready |

**Development Tools:** UV, Ruff, MyPy, Pytest, Docker Compose

### **🏗️ Project Structure**

```
production-agentic-rag-course/
├── src/                    # Main application code
│   ├── main.py             # FastAPI app; creates all services at startup
│   ├── dependencies.py     # FastAPI dependency injection for services
│   ├── routers/            # API endpoints (health, hybrid search, ask/stream, agentic ask)
│   ├── services/           # Business logic (arxiv, pdf_parser, indexing, embeddings,
│   │                       #   opensearch, ollama, cache, langfuse, agents, telegram)
│   ├── db/                 # Database connection (PostgreSQL)
│   ├── repositories/       # Data access for papers
│   ├── models/             # Database models (SQLAlchemy)
│   ├── schemas/            # Pydantic validation schemas
│   ├── gradio_app.py       # Gradio chat UI
│   └── config.py           # Environment configuration
├── notebooks/              # Weekly learning materials (week1-7)
├── airflow/                # Workflow orchestration (DAGs, Airflow Dockerfile)
├── tests/                  # Test suite (unit, api, integration)
├── static/                 # Architecture diagrams
├── gradio_launcher.py      # Starts the Gradio UI on port 7861
└── compose.yml             # Docker service orchestration
```

### **📡 API Endpoints Reference**

| Endpoint | Method | Description | Week |
|----------|--------|-------------|------|
| `/api/v1/health` | GET | Health check for the API, database, OpenSearch, and Ollama | Week 1 |
| `/api/v1/hybrid-search/` | POST | Search paper chunks: hybrid (BM25 + vector), or BM25 only with `"use_hybrid": false` | Week 3–4 |
| `/api/v1/ask` | POST | RAG question answering with sources (Redis-cached) | **Week 5** |
| `/api/v1/stream` | POST | Streaming RAG answer (`data: {...}` lines) | **Week 5** |
| `/api/v1/ask-agentic` | POST | Agentic RAG with guardrails, document grading, and query rewriting | **Week 7** |
| `/api/v1/feedback` | POST | Submit a score/comment for a response's Langfuse `trace_id` | **Week 7** |

Example:
```bash
curl -X POST http://localhost:8000/api/v1/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What are transformers in machine learning?", "top_k": 3, "use_hybrid": true}'
```

Paper data is loaded by the Airflow ingestion DAG, not through the API. Unpause and trigger `arxiv_paper_ingestion` in the Airflow UI to populate PostgreSQL and OpenSearch.

**API Documentation:** Visit http://localhost:8000/docs for interactive API explorer

### **🔧 Essential Commands**

#### **Using the Makefile** (Recommended)
```bash
# View all available commands
make help

# Quick workflow
make start         # Start all services
make health        # Check all services health
make test          # Run tests
make stop          # Stop services
```

#### **All Available Commands**
| Command | Description |
|---------|-------------|
| `make start` | Start all services |
| `make stop` | Stop all services |
| `make restart` | Restart all services |
| `make status` | Show service status |
| `make logs` | Show service logs |
| `make health` | Check all services health |
| `make setup` | Install Python dependencies |
| `make format` | Format code |
| `make lint` | Lint and type check |
| `make test` | Run tests |
| `make test-cov` | Run tests with coverage |
| `make clean` | Clean up everything |

#### **Direct Commands** (Alternative)
```bash
# If you prefer using commands directly
docker compose up --build -d      # Start services
docker compose up --build -d api  # Rebuild the API after changing src/ (code is copied into the image)
docker compose ps                 # Check status
docker compose logs               # View logs
uv run pytest                     # Run tests
uv run pytest tests/unit          # Unit tests only (no running services needed)
```

### **🎓 Target Audience**
| Who | Why |
|-----|-----|
| **AI/ML Engineers** | Learn production RAG architecture beyond tutorials |
| **Software Engineers** | Build end-to-end AI applications with best practices |
| **Data Scientists** | Implement production AI systems using modern tools |

---

## 🛠️ Troubleshooting

**Common Issues:**
- **Services not starting?** Wait 2-3 minutes, check `docker compose logs`
- **Port conflicts?** Stop other services using ports 8000, 8080, 5432, 9200, 6379, 3001, 11434
- **Memory issues?** Increase Docker Desktop memory allocation
- **Ollama "model not found"?** Pull the model: `docker exec rag-ollama ollama pull llama3.2:1b` (check with `docker exec rag-ollama ollama list`)
- **Search returns no results?** The index is empty until the Airflow DAG has run, and search errors are logged rather than returned, so check `docker compose logs api`
- **Code changes not showing up?** Rebuild the API: `docker compose up --build -d api`

**Get Help:**
- Check the comprehensive Week 1 notebook troubleshooting section
- Review service logs: `docker compose logs [service-name]`
- Complete reset: `docker compose down --volumes && docker compose up --build -d`

---

## 💰 Cost Structure

**This course is completely free!** You'll only need minimal costs for optional services:
- **Local Development:** $0 (everything runs locally)
- **Optional Cloud APIs:** ~$2-5 for external LLM services (if chosen)

---

<div align="center">
  <h3>🎉 Ready to Start Your AI Engineering Journey?</h3>
  <p><strong>Begin with the Week 1 setup notebook and build your first production RAG system!</strong></p>
  
  <p><em>For learners who want to master modern AI engineering</em></p>
  <p><strong>Built with love by <a href="https://www.linkedin.com/in/shirin-khosravi-jam/">Shirin Khosravi Jam</a> & <a href="https://www.linkedin.com/in/shantanuladhwe/">Shantanu Ladhwe</a></strong></p>
</div>

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jamwithai/production-agentic-rag-course&type=Date)](https://star-history.com/#jamwithai/production-agentic-rag-course&Date)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.
