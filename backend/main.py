"""
Smriti Backend - FastAPI Application
Private AI for your documents
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from contextlib import asynccontextmanager
import os
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

# Import routers
from api import documents, search

# Configuration and database
from config import settings, ensure_directories
from db.database import init_db
from services.llm.ollama_service import check_ollama_connection


# Lifespan context manager for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Smriti Backend Starting...")
    print(f"📚 Database: {settings.database_url}")
    print(f"🤖 Ollama: {settings.ollama_base_url}")
    print(f"📁 Upload directory: {settings.upload_dir}")
    
    # Ensure directories exist
    ensure_directories()
    
    # Initialize database
    init_db()
    
    # Check Ollama connection
    ollama_connected = await check_ollama_connection()
    if ollama_connected:
        print("✅ Ollama connection successful")
    else:
        print("⚠️  Ollama not available - AI features will be limited")
    
    print("✅ Smriti Backend ready!")
    
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
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(documents.router, prefix="/api")
app.include_router(search.router, prefix="/api")

# Root endpoint
@app.get("/")
async def root():
    return {
        "name": "Smriti API",
        "version": "1.0.0",
        "description": "Private AI for your documents",
        "tagline": "Local-first AI knowledge operating system",
        "status": "running"
    }

# Health check
@app.get("/health")
async def health_check():
    # Check Ollama
    ollama_status = await check_ollama_connection()
    
    return {
        "status": "healthy",
        "database": "connected",
        "ollama": "connected" if ollama_status else "disconnected",
        "vector_store": "ready",
        "features": {
            "document_upload": True,
            "semantic_search": True,
            "rag_qa": ollama_status,
            "citations": True,
            "local_ai": ollama_status
        }
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
            "llm": settings.default_model,
            "embedding": settings.default_embedding_model
        },
        "limits": {
            "max_file_size": f"{settings.max_file_size / 1024 / 1024}MB",
            "chunk_size": settings.chunk_size,
            "chunk_overlap": settings.chunk_overlap
        }
    }

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
        app,  # Pass app object directly instead of string
        host=settings.host,
        port=settings.port,
        reload=False  # Disable reload to avoid module import issues
    )
