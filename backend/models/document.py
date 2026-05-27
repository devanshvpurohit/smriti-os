"""
Document and Chunk Models
SQLAlchemy ORM models for document storage
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship
from datetime import datetime
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from db.database import Base


class Document(Base):
    """Document metadata"""
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    file_type = Column(String(50), nullable=False)  # pdf, docx, txt, md, eml
    file_size = Column(Integer, nullable=False)  # bytes
    file_path = Column(String(500), nullable=False)
    
    # Processing status
    status = Column(String(50), default="processing")  # processing, completed, failed
    chunks_count = Column(Integer, default=0)
    
    # Extra metadata
    extra_metadata = Column(JSON, nullable=True)  # Additional metadata (author, date, etc.)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    chunks = relationship("Chunk", back_populates="document", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Document(id={self.id}, filename='{self.filename}')>"


class Chunk(Base):
    """Document chunks for RAG"""
    __tablename__ = "chunks"
    
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    
    # Chunk content
    content = Column(Text, nullable=False)
    chunk_index = Column(Integer, nullable=False)  # Position in document
    
    # Chunk metadata
    page_number = Column(Integer, nullable=True)
    section_title = Column(String(500), nullable=True)
    
    # Vector embedding ID (stored in ChromaDB)
    vector_id = Column(String(100), nullable=True, index=True)
    
    # Extra metadata
    extra_metadata = Column(JSON, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    document = relationship("Document", back_populates="chunks")
    
    def __repr__(self):
        return f"<Chunk(id={self.id}, document_id={self.document_id}, index={self.chunk_index})>"
