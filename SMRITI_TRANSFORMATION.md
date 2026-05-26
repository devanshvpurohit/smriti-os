# Smriti Transformation Plan

## Overview
Transforming Puter into Smriti - A Private AI Knowledge Operating System

**Original**: Puter - Desktop environment in the browser
**New**: Smriti - Private AI for your documents

---

## Step 1: Fork & Rebrand ✅ IN PROGRESS

### Completed
- ✅ Cloned Puter repository
- ✅ Renamed to `smriti-os`
- ✅ Updated package.json metadata

### In Progress
- 🔄 Update README.md
- 🔄 Update branding strings
- 🔄 Replace logos and icons
- 🔄 Update landing page text

### Files to Update
- [x] `/package.json` - Name, description, homepage
- [ ] `/README.md` - Complete rewrite
- [ ] `/src/gui/src/index.html` - Title, meta tags
- [ ] `/src/gui/src/` - UI strings and branding
- [ ] Logo files and icons
- [ ] Configuration files

---

## Step 2: Clean the Fork (NEXT)

### Keep
- ✅ UI shell and window system
- ✅ Local filesystem support
- ✅ Auth/session logic
- ✅ App layout system
- ✅ Desktop environment framework

### Remove
- ❌ Cloud storage features
- ❌ App store integration
- ❌ Unnecessary Puter-specific apps
- ❌ Social features
- ❌ Monetization features
- ❌ Multi-tenant cloud features

---

## Step 3: Create New Project Structure

### New Directories to Add
```
/backend/
  /api/          # FastAPI routes
  /services/     # Business logic
    /ingestion/  # Document processing
    /retrieval/  # RAG retrieval
    /reranking/  # Result reranking
    /citations/  # Citation engine
    /llm/        # Ollama integration
  /models/       # Data models
  /db/           # Database setup
  /utils/        # Utilities
/docker/         # Docker configs
/docs/           # Documentation
```

---

## Step 4-20: Feature Implementation

Following the roadmap:
- Step 4: FastAPI backend
- Step 5: SQLite database
- Step 6: Ollama integration
- Step 7: Document ingestion
- Step 8: Chunking system
- Step 9: Embeddings
- Step 10: ChromaDB
- Step 11: RAG pipeline
- Step 12: Citation engine
- Step 13: Anti-hallucination
- Step 14: Search experience
- Step 15: Chat experience
- Step 16: Modern UI
- Step 17: Settings panel
- Step 18: Docker support
- Step 19: Open source prep
- Step 20: Positioning & branding

---

## Key Differentiators

### Puter → Smriti
| Feature | Puter | Smriti |
|---------|-------|--------|
| **Purpose** | Cloud desktop OS | AI knowledge OS |
| **Storage** | Cloud files | Local documents + AI |
| **Apps** | Web apps | AI-powered document tools |
| **Backend** | Node.js | FastAPI + Ollama |
| **Focus** | General computing | Document intelligence |
| **AI** | Optional | Core feature |
| **Privacy** | Cloud-first | Local-first |

---

## Branding Guidelines

### Name
**Smriti** (Sanskrit: स्मृति)
- Meaning: "Memory" or "Remembrance"
- Pronunciation: SMRI-tee

### Tagline
**"Private AI for your documents"**

### Alternative Taglines
- "Your Private Knowledge Operating System"
- "Local AI that remembers everything"
- "Document intelligence, privately"

### Color Scheme
- Primary: Deep Blue (#1E3A8A)
- Secondary: Indigo (#4F46E5)
- Accent: Cyan (#06B6D4)
- Background: Dark (#0F172A)
- Text: Light Gray (#E2E8F0)

### Logo Concept
- Brain + Document icon
- Minimalist, modern design
- Works in light and dark mode

---

## Technical Architecture

### Frontend (Keep from Puter)
- Desktop-style UI framework
- Window management system
- File browser interface
- Modern, responsive design

### Backend (New - FastAPI)
```
FastAPI Backend
├── Document Ingestion
├── Ollama Integration
├── RAG Pipeline
├── Citation Engine
└── Vector Store (ChromaDB)
```

### Data Flow
```
User uploads document
    ↓
Parse & chunk
    ↓
Generate embeddings (local)
    ↓
Store in ChromaDB
    ↓
User asks question
    ↓
Retrieve relevant chunks
    ↓
Rerank results
    ↓
Generate answer with Ollama
    ↓
Return with citations
```

---

## Development Phases

### Phase 1: Foundation (Current)
- Fork and rebrand
- Clean unnecessary features
- Set up new project structure

### Phase 2: Backend Core
- FastAPI setup
- Database integration
- Ollama connection
- Basic API routes

### Phase 3: Document Pipeline
- Upload system
- Parsing (PDF, DOCX, etc.)
- Chunking
- Embedding generation
- Vector storage

### Phase 4: RAG System
- Retrieval logic
- Reranking
- LLM integration
- Citation extraction

### Phase 5: UI Integration
- Adapt Puter's UI
- Document viewer
- Chat interface
- Citation display

### Phase 6: Polish & Launch
- Testing
- Documentation
- Docker setup
- Open source release

---

## Success Metrics

### Technical
- ✅ 100% local processing
- ✅ Sub-second search
- ✅ Accurate citations
- ✅ No hallucinations
- ✅ Offline capable

### User Experience
- ✅ One-command install
- ✅ Beautiful UI
- ✅ Intuitive workflow
- ✅ Fast responses
- ✅ Trustworthy results

---

## Next Steps

1. ✅ Complete README rewrite
2. Update all branding strings
3. Remove unnecessary Puter features
4. Set up FastAPI backend structure
5. Integrate Ollama
6. Build document ingestion pipeline

---

**Status**: Step 1 in progress
**Last Updated**: 2026-05-19
