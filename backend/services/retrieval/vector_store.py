"""
Vector Store Service
Management of ChromaDB collections and document embeddings
"""

import chromadb
from chromadb.config import Settings as ChromaSettings
from sentence_transformers import SentenceTransformer
import os
from typing import List, Dict, Any, Optional
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(backend_dir))

from config import settings

# Global instances
_chroma_client = None
_embedding_model = None


def get_chroma_client():
    """Get or create ChromaDB client"""
    global _chroma_client
    if _chroma_client is None:
        _chroma_client = chromadb.PersistentClient(path=settings.chroma_persist_dir)
    return _chroma_client


def get_embedding_model():
    """Get or create SentenceTransformer model"""
    global _embedding_model
    if _embedding_model is None:
        # Load model (will download if not present)
        _embedding_model = SentenceTransformer(settings.default_embedding_model)
    return _embedding_model


def get_collection():
    """Get or create Smriti collection"""
    client = get_chroma_client()
    return client.get_or_create_collection(name=settings.collection_name)


async def add_to_vector_store(chunks: List[Dict[str, Any]], document_id: int):
    """
    Generate embeddings and add chunks to ChromaDB
    
    Args:
        chunks: List of chunk data (content, page_number, etc.)
        document_id: ID of the parent document
    """
    collection = get_collection()
    model = get_embedding_model()
    
    ids = []
    documents = []
    metadatas = []
    
    for idx, chunk in enumerate(chunks):
        chunk_id = f"doc_{document_id}_chunk_{idx}"
        ids.append(chunk_id)
        documents.append(chunk["content"])
        
        # Prepare metadata
        metadata = {
            "document_id": document_id,
            "filename": chunk["metadata"]["filename"],
            "chunk_index": idx,
        }
        if chunk.get("page_number"):
            metadata["page_number"] = chunk["page_number"]
        if chunk.get("section_title"):
            metadata["section_title"] = chunk["section_title"]
            
        metadatas.append(metadata)
    
    # Generate embeddings
    embeddings = model.encode(documents).tolist()
    
    # Add to collection
    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas
    )
    
    return ids


async def query_vector_store(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Search vector store for relevant chunks
    """
    collection = get_collection()
    model = get_embedding_model()
    
    # Generate query embedding
    query_embedding = model.encode([query]).tolist()[0]
    
    # Query ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=limit
    )
    
    # Format results
    formatted_results = []
    for i in range(len(results["ids"][0])):
        formatted_results.append({
            "chunk_id": results["ids"][0][i],
            "document_id": results["metadatas"][0][i]["document_id"],
            "filename": results["metadatas"][0][i]["filename"],
            "content": results["documents"][0][i],
            "page_number": results["metadatas"][0][i].get("page_number"),
            "section_title": results["metadatas"][0][i].get("section_title"),
            "similarity_score": 1.0 - results["distances"][0][i],  # Convert distance to similarity
            "metadata": results["metadatas"][0][i]
        })
        
    return formatted_results


async def delete_from_vector_store(document_id: int):
    """
    Delete all chunks of a document from vector store
    """
    collection = get_collection()
    collection.delete(
        where={"document_id": document_id}
    )
