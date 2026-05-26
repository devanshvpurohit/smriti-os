"""
Smriti Backend - FastAPI Application
Private AI for your documents
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from contextlib import asynccontextmanager

# Import routers (will be created)
# from api import documents, search, settings, health

# Configuration
from dotenv import load_dotenv
import os

load_dotenv()

# Lifespan context manager for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Smriti Backend Starting...")
    print(f"📚 Database: {os.getenv('DATABASE_URL', 'sqlite:///./data/smriti.db')}")
    print(f"🤖 Ollama: {os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')}")
    print(f"📁 Upload directory: {os.getenv('UPLOAD_DIR', './uploads')}")
    
    # Initialize database
    # await init_db()
    
    # Initialize vector store
    # await init_vector_store()
    
    # Check Ollama connection
    # await check_ollama()
    
    yield
    
    # Shutdown
    print("👋 Smriti Backend Shutting Down...")

# Create FastAPI app
app = FastAPI(
    title="Smriti API",
    description="Private AI for your documents - Local-first AI knowledge operating system",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Configuration
origins = os.getenv("CORS_ORIGINS", "http://localhost:4100").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {
        "name": "Smriti API",
        "version": "1.0.0",
        "description": "Private AI for your documents",
        "status": "running"
    }

# Health check
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": "connected",  # TODO: Check actual DB connection
        "ollama": "connected",     # TODO: Check actual Ollama connection
        "vector_store": "ready"    # TODO: Check actual ChromaDB status
    }

# API Info
@app.get("/api/info")
async def api_info():
    return {
        "name": "Smriti",
        "tagline": "Private AI for your documents",
        "version": "1.0.0",
        "features": {
            "document_upload": True,
            "semantic_search": True,
            "rag_qa": True,
            "citations": True,
            "local_ai": True,
            "offline_mode": True
        },
        "supported_formats": ["pdf", "docx", "txt", "md", "eml", "html"],
        "ai_models": {
            "llm": os.getenv("DEFAULT_MODEL", "mistral"),
            "embedding": os.getenv("DEFAULT_EMBEDDING_MODEL", "all-MiniLM-L6-v2")
        }
    }

# Include routers (will be added as we build them)
# app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
# app.include_router(search.router, prefix="/api/search", tags=["Search"])
# app.include_router(settings.router, prefix="/api/settings", tags=["Settings"])

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"error": "Not found", "detail": str(exc)}
    )

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

# Run server
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=os.getenv("DEBUG", "true").lower() == "true"
    )
