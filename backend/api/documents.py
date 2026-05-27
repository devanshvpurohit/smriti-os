"""
Document Management API Routes
Upload, list, delete documents
"""

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import os
import shutil
from datetime import datetime
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from db.database import get_db
from models.document import Document
from services.ingestion.document_processor import process_document
from config import settings

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Upload and process a document
    Supported formats: PDF, DOCX, TXT, MD, EML
    """
    # Validate file size
    file_size = 0
    content = await file.read()
    file_size = len(content)
    
    if file_size > settings.max_file_size:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Maximum size: {settings.max_file_size / 1024 / 1024}MB"
        )
    
    # Validate file type
    allowed_extensions = ['.pdf', '.docx', '.txt', '.md', '.eml', '.html']
    file_ext = os.path.splitext(file.filename)[1].lower()
    
    if file_ext not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type. Allowed: {', '.join(allowed_extensions)}"
        )
    
    # Save file
    file_path = os.path.join(settings.upload_dir, file.filename)
    
    # Ensure upload directory exists
    os.makedirs(settings.upload_dir, exist_ok=True)
    
    with open(file_path, "wb") as f:
        f.write(content)
    
    try:
        # Process document (extract text, chunk, embed)
        doc_data = await process_document(file_path, file.filename, db)
        
        return {
            "message": "Document uploaded and processed successfully",
            "document_id": doc_data["id"],
            "filename": file.filename,
            "chunks": doc_data["chunks_count"],
            "status": "processed"
        }
    
    except Exception as e:
        # Clean up file if processing fails
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")


@router.get("/")
async def list_documents(db: Session = Depends(get_db)):
    """List all uploaded documents"""
    documents = db.query(Document).order_by(Document.created_at.desc()).all()
    
    return {
        "documents": [
            {
                "id": doc.id,
                "filename": doc.filename,
                "file_type": doc.file_type,
                "file_size": doc.file_size,
                "chunks_count": doc.chunks_count,
                "status": doc.status,
                "created_at": doc.created_at.isoformat(),
            }
            for doc in documents
        ],
        "total": len(documents)
    }


@router.get("/{document_id}")
async def get_document(document_id: int, db: Session = Depends(get_db)):
    """Get document details"""
    document = db.query(Document).filter(Document.id == document_id).first()
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return {
        "id": document.id,
        "filename": document.filename,
        "file_type": document.file_type,
        "file_size": document.file_size,
        "file_path": document.file_path,
        "chunks_count": document.chunks_count,
        "status": document.status,
        "created_at": document.created_at.isoformat(),
        "extra_metadata": document.extra_metadata
    }


@router.delete("/{document_id}")
async def delete_document(document_id: int, db: Session = Depends(get_db)):
    """Delete a document and its chunks"""
    document = db.query(Document).filter(Document.id == document_id).first()
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # Delete file from disk
    if os.path.exists(document.file_path):
        os.remove(document.file_path)
    
    # Delete from database (chunks will be cascade deleted)
    db.delete(document)
    db.commit()
    
    # Delete from vector store
    from services.retrieval.vector_store import delete_from_vector_store
    await delete_from_vector_store(document_id)
    
    return {
        "message": "Document deleted successfully",
        "document_id": document_id
    }
