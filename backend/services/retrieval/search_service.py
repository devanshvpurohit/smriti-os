"""
Search and Retrieval Service
Semantic search using vector embeddings
"""

from typing import List, Dict
from sqlalchemy.orm import Session
from sqlalchemy import func
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(backend_dir))

from models.document import Chunk, Document
from services.retrieval.vector_store import query_vector_store


async def semantic_search(query: str, limit: int, db: Session) -> List[Dict]:
    """
    Perform semantic search across document chunks using vector embeddings
    """
    return await query_vector_store(query, limit)



async def hybrid_search(query: str, limit: int, db: Session) -> List[Dict]:
    """
    Hybrid search combining semantic and keyword search
    TODO: Implement actual hybrid search
    """
    # For now, just use semantic search
    return await semantic_search(query, limit, db)
