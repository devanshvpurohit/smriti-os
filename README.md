<h3 align="center"><img width="80" alt="Smriti - Private AI for your documents" src="https://via.placeholder.com/80x80/1E3A8A/FFFFFF?text=S"></h3>

<h3 align="center">Private AI for Your Documents</h3>

<p align="center">
    <strong>Local-first AI Knowledge Operating System</strong>
    <br />
    <br />
    <a href="#-features">Features</a>
    ·
    <a href="#-getting-started">Getting Started</a>
    ·
    <a href="#-how-it-works">How It Works</a>
    ·
    <a href="#-documentation">Documentation</a>
</p>

<h3 align="center"><img width="800" style="border-radius:5px;" alt="Smriti Screenshot" src="https://via.placeholder.com/800x450/0F172A/E2E8F0?text=Smriti+Screenshot"></h3>

<br/>

## What is Smriti?

**Smriti** (Sanskrit: स्मृति, meaning "memory") is a privacy-first AI knowledge operating system that lets you upload documents and ask questions across them using natural language with **accurate source citations**.

Built on top of [Puter](https://github.com/HeyPuter/puter)'s desktop OS framework, Smriti transforms your documents into an intelligent, searchable knowledge base that runs **100% locally** on your machine.

### 🎯 Core Philosophy

**Trust Through Traceability**

Every answer includes:
- ✅ Exact source file
- ✅ Page number
- ✅ Paragraph snippet
- ✅ Confidence score
- ✅ Highlighted evidence

**Privacy First**

- 🔒 All data stays on your machine
- 🔒 Local AI processing with Ollama
- 🔒 No cloud uploads
- 🔒 Fully self-hosted
- 🔒 Offline capable

<br/>

## ✨ Features

### 🤖 Local AI Processing
- Powered by **Ollama** (Llama 3, Mistral, Phi, DeepSeek)
- 100% local inference
- No API keys required
- Works offline
- Privacy guaranteed

### 📄 Document Intelligence
- **Upload**: PDF, DOCX, TXT, Markdown, Email (.eml)
- **Parse**: Automatic text extraction with OCR fallback
- **Index**: Semantic embeddings for intelligent search
- **Search**: Natural language queries across all documents
- **Cite**: Every answer includes exact sources

### 🔍 Advanced RAG Pipeline
- Semantic search with vector embeddings
- Hybrid retrieval (semantic + keyword)
- Result reranking for accuracy
- Context-aware answer generation
- Anti-hallucination safeguards

### 💬 Chat Interface
- Streaming responses
- Markdown rendering
- Syntax highlighting
- Expandable citations
- Evidence cards
- Confidence scoring

### 🖥️ Desktop OS Experience
- Window management system
- File browser interface
- Drag & drop uploads
- Modern, responsive UI
- Dark mode support
- Glassmorphism design

### 🛡️ Anti-Hallucination System
- Confidence thresholds
- Source verification
- "I don't know" responses when uncertain
- No fabricated citations
- Retrieval quality checks

<br/>

## 🚀 Getting Started

### Prerequisites

- **Node.js** >= 24.0.0
- **Python** >= 3.10
- **Ollama** ([Install here](https://ollama.ai))

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/smriti.git
cd smriti

# 2. Install dependencies
npm install

# 3. Install Python dependencies
cd backend
pip install -r requirements.txt

# 4. Pull an Ollama model
ollama pull mistral

# 5. Start Smriti
npm start
```

**→** This will launch Smriti at http://localhost:4100

### Docker Setup

```bash
# One-command startup
docker compose up
```

<br/>

## 📖 How It Works

### 1. Document Ingestion
```
Upload Document → Parse Content → Extract Text → Chunk Intelligently
```

### 2. Embedding Generation
```
Text Chunks → Local Embeddings (sentence-transformers) → ChromaDB Storage
```

### 3. Question Answering
```
User Question → Semantic Search → Retrieve Chunks → Rerank Results
                                                          ↓
Answer with Citations ← Generate Response ← Ollama LLM ← Context
```

### 4. Citation Extraction
```
Generated Answer → Extract Sources → Link to Original → Highlight Evidence
```

<br/>

## 🎨 Supported File Types

| Format | Support | OCR Fallback |
|--------|---------|--------------|
| PDF | ✅ | ✅ |
| DOCX | ✅ | - |
| TXT | ✅ | - |
| Markdown | ✅ | - |
| Email (.eml) | ✅ | - |
| HTML | ✅ | - |

<br/>

## 🏗️ Architecture

### Frontend
- **Base**: Puter's desktop OS framework
- **UI**: Modern, responsive, window-based interface
- **Features**: File management, chat interface, citation viewer

### Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLite (metadata) + ChromaDB (vectors)
- **AI**: Ollama (local LLM inference)
- **Embeddings**: sentence-transformers (local)
- **RAG**: LangChain / LlamaIndex

### Data Flow
```
┌─────────────┐
│   Browser   │
│  (Puter UI) │
└──────┬──────┘
       │
       ↓
┌─────────────┐
│   FastAPI   │
│   Backend   │
└──────┬──────┘
       │
       ├──→ SQLite (metadata)
       ├──→ ChromaDB (vectors)
       └──→ Ollama (LLM)
```

<br/>

## 🛠️ Configuration

### Environment Variables

```bash
# Backend (.env)
DATABASE_URL=sqlite:///./data/smriti.db
OLLAMA_BASE_URL=http://localhost:11434
DEFAULT_MODEL=mistral
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

### Ollama Models

```bash
# Recommended models
ollama pull mistral      # Balanced performance
ollama pull llama3       # High quality
ollama pull phi          # Fast, lightweight
ollama pull deepseek     # Code-focused
```

<br/>

## 📚 Documentation

- [Installation Guide](./docs/installation.md)
- [Architecture Overview](./docs/architecture.md)
- [API Reference](./docs/api.md)
- [Development Guide](./docs/development.md)
- [Self-Hosting](./docs/self-hosting.md)

<br/>

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Install dependencies
npm install

# Start backend in dev mode
cd backend
python -m uvicorn app.main:app --reload

# Start frontend in dev mode
npm run dev
```

<br/>

## 🔒 Security

- All processing happens locally
- No data leaves your machine
- No telemetry or tracking
- Open source and auditable
- Self-hosted by default

For security issues, please email: security@smriti.dev

<br/>

## 📄 License

This project is licensed under [AGPL-3.0](./LICENSE.txt).

Built on top of [Puter](https://github.com/HeyPuter/puter) - Desktop environment in the browser.

<br/>

## 🙏 Acknowledgments

- **Puter** - For the amazing desktop OS framework
- **Ollama** - For making local AI accessible
- **ChromaDB** - For vector storage
- **LangChain** - For RAG tooling
- **FastAPI** - For the backend framework

<br/>

## 🌟 Why Smriti?

### vs. ChatGPT
- ✅ **Privacy**: Your documents never leave your machine
- ✅ **Citations**: Every answer includes exact sources
- ✅ **Offline**: Works without internet
- ✅ **Free**: No API costs

### vs. Notion AI
- ✅ **Local**: No cloud dependency
- ✅ **Open Source**: Fully auditable
- ✅ **Self-Hosted**: You own your data
- ✅ **Customizable**: Extend as needed

### vs. Obsidian + AI Plugins
- ✅ **Desktop OS**: Full window management
- ✅ **RAG Pipeline**: Advanced retrieval
- ✅ **Citations**: Built-in source tracking
- ✅ **Multi-Format**: PDF, DOCX, and more

<br/>

## 🎯 Roadmap

### v1.0 (Current)
- [x] Fork Puter
- [x] Rebrand to Smriti
- [ ] FastAPI backend
- [ ] Ollama integration
- [ ] Document ingestion
- [ ] RAG pipeline
- [ ] Citation engine
- [ ] UI integration

### v1.1
- [ ] Multi-language support
- [ ] Advanced chunking strategies
- [ ] Custom embedding models
- [ ] Export functionality
- [ ] Batch processing

### v2.0
- [ ] Multi-user workspaces
- [ ] Collaborative annotations
- [ ] Mobile app
- [ ] Browser extension
- [ ] Cloud sync (optional)

<br/>

## 💬 Community

- **Discord**: [Join our server](#)
- **Twitter**: [@SmritiAI](#)
- **Reddit**: [r/smriti](#)
- **Email**: hi@smriti.dev

<br/>

---

<p align="center">
  <strong>Smriti</strong> - Private AI for your documents
  <br/>
  Built with ❤️ for privacy and trust
</p>

<p align="center">
  <a href="#-getting-started">Get Started</a> •
  <a href="./docs">Documentation</a> •
  <a href="./CONTRIBUTING.md">Contribute</a>
</p>
