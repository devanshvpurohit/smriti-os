# Smriti Quick Start Guide

## 🚀 Get Smriti Running in 5 Minutes

### Prerequisites

Before you begin, ensure you have:
- **Node.js** >= 18.0.0 ([Download](https://nodejs.org/))
- **Python** >= 3.10 ([Download](https://python.org/))
- **Ollama** ([Install](https://ollama.ai/))
- **Git** ([Download](https://git-scm.com/))

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/smriti.git
cd smriti
```

---

## Step 2: Install Frontend Dependencies

```bash
# Install Node.js dependencies
npm install
```

This will install ~1,285 packages (takes 1-2 minutes).

---

## Step 3: Set Up Backend

### 3.1 Create Python Virtual Environment

```bash
cd backend
python -m venv venv
```

### 3.2 Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3.3 Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install FastAPI, ChromaDB, LangChain, and other dependencies.

### 3.4 Create Environment File

```bash
cp .env.example .env
```

Edit `.env` if needed (defaults work for local development).

---

## Step 4: Install and Configure Ollama

### 4.1 Install Ollama

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download from [ollama.ai](https://ollama.ai/)

### 4.2 Start Ollama Service

```bash
ollama serve
```

Keep this terminal open.

### 4.3 Pull a Model

In a new terminal:
```bash
ollama pull mistral
```

Other recommended models:
```bash
ollama pull llama3      # High quality
ollama pull phi         # Fast, lightweight
ollama pull deepseek    # Code-focused
```

---

## Step 5: Start Smriti

### 5.1 Start Backend (Terminal 1)

```bash
cd backend
source venv/bin/activate  # If not already activated
python main.py
```

You should see:
```
🚀 Smriti Backend Starting...
📚 Database: sqlite:///./data/smriti.db
🤖 Ollama: http://localhost:11434
📁 Upload directory: ./uploads
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 5.2 Start Frontend (Terminal 2)

```bash
# From project root
npm start
```

You should see:
```
Smriti is running at:
  → http://puter.localhost:4100
  → http://localhost:4100
```

---

## Step 6: Open Smriti

Open your browser and navigate to:
- **http://localhost:4100** or
- **http://puter.localhost:4100**

You should see the Smriti desktop interface!

---

## 🧪 Test the Installation

### Test Backend API

```bash
# Test root endpoint
curl http://localhost:8000/

# Test health check
curl http://localhost:8000/health

# Test API info
curl http://localhost:8000/api/info
```

### Test Ollama

```bash
curl http://localhost:11434/api/tags
```

Should return list of installed models.

### View API Documentation

Open in browser:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 📁 Project Structure

```
smriti/
├── src/
│   ├── gui/              # Frontend (Puter-based)
│   └── puter-js/         # Puter SDK
├── backend/              # FastAPI backend
│   ├── api/              # API routes
│   ├── services/         # Business logic
│   ├── models/           # Data models
│   ├── db/               # Database
│   ├── main.py           # FastAPI app
│   └── config.py         # Configuration
├── docker/               # Docker configs
├── docs/                 # Documentation
└── README.md
```

---

## 🔧 Configuration

### Backend Configuration (backend/.env)

```env
# Server
HOST=0.0.0.0
PORT=8000
DEBUG=true

# Database
DATABASE_URL=sqlite:///./data/smriti.db

# Ollama
OLLAMA_BASE_URL=http://localhost:11434
DEFAULT_MODEL=mistral
DEFAULT_EMBEDDING_MODEL=all-MiniLM-L6-v2

# Document Processing
MAX_FILE_SIZE=104857600  # 100MB
CHUNK_SIZE=512
CHUNK_OVERLAP=50

# Features
ENABLE_OCR=true
ENABLE_RERANKING=true
```

---

## 🐛 Troubleshooting

### Backend won't start

**Error:** `ModuleNotFoundError`
```bash
# Make sure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**Error:** `Port 8000 already in use`
```bash
# Change port in .env
PORT=8001
```

### Frontend won't start

**Error:** `Port 4100 already in use`
```bash
# Kill the process
lsof -i :4100
kill -9 <PID>
```

**Error:** `npm install fails`
```bash
# Clear cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### Ollama not responding

**Error:** `Connection refused`
```bash
# Start Ollama service
ollama serve

# Check if running
curl http://localhost:11434/api/tags
```

**Error:** `Model not found`
```bash
# Pull the model
ollama pull mistral
```

### Database errors

```bash
# Delete and recreate database
rm -rf backend/data/
python backend/main.py  # Will recreate on startup
```

---

## 🎯 Next Steps

Now that Smriti is running:

1. **Upload a Document**
   - Click "Upload" in the UI
   - Select a PDF, DOCX, or TXT file
   - Wait for processing

2. **Ask a Question**
   - Type a question in the chat interface
   - Get an answer with citations

3. **Explore Features**
   - View indexed documents
   - Search semantically
   - Check citations
   - Adjust settings

4. **Read Documentation**
   - [Architecture](./docs/architecture.md)
   - [API Reference](./docs/api.md)
   - [Development Guide](./docs/development.md)

---

## 🚀 Development Mode

### Hot Reload

Both frontend and backend support hot reload:

**Backend:**
```bash
# Already enabled with --reload flag
python main.py
```

**Frontend:**
```bash
# Already enabled with npm start
npm start
```

### Run Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
npm test
```

---

## 🐳 Docker Quick Start (Alternative)

If you prefer Docker:

```bash
# Build and start all services
docker compose up

# Access Smriti
open http://localhost:4100
```

---

## 📚 Learn More

- [Full Documentation](./README.md)
- [Architecture Overview](./docs/architecture.md)
- [API Reference](./docs/api.md)
- [Contributing Guide](./CONTRIBUTING.md)

---

## 🆘 Get Help

- **Issues:** [GitHub Issues](https://github.com/yourusername/smriti/issues)
- **Discord:** [Join our server](#)
- **Email:** hi@smriti.dev

---

## ✅ Checklist

- [ ] Node.js >= 18.0.0 installed
- [ ] Python >= 3.10 installed
- [ ] Ollama installed and running
- [ ] Frontend dependencies installed (`npm install`)
- [ ] Backend dependencies installed (`pip install -r requirements.txt`)
- [ ] Ollama model pulled (`ollama pull mistral`)
- [ ] Backend running on port 8000
- [ ] Frontend running on port 4100
- [ ] Can access http://localhost:4100
- [ ] API docs accessible at http://localhost:8000/docs

---

**You're all set! Start building your private AI knowledge base! 🎉**
