"""
Search and RAG API Routes
Semantic search and question answering
"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from db.database import get_db
from services.retrieval.search_service import semantic_search
from services.llm.ollama_service import generate_answer
from services.citations.citation_service import extract_citations

router = APIRouter(prefix="/search", tags=["Search"])


class SearchRequest(BaseModel):
    query: str
    limit: int = 5


class AskRequest(BaseModel):
    question: str
    model: Optional[str] = None
    stream: bool = False


@router.post("/")
async def search_documents(
    request: SearchRequest,
    db: Session = Depends(get_db)
):
    """
    Semantic search across all documents
    Returns relevant chunks with similarity scores
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    try:
        results = await semantic_search(
            query=request.query,
            limit=request.limit,
            db=db
        )
        
        return {
            "query": request.query,
            "results": results,
            "count": len(results)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@router.post("/ask")
async def ask_question(
    request: AskRequest,
    db: Session = Depends(get_db)
):
    """
    Ask a question using RAG
    Retrieves relevant context and generates answer with citations
    """
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    try:
        # 1. Retrieve relevant chunks
        search_results = await semantic_search(
            query=request.question,
            limit=5,
            db=db
        )
        
        if not search_results:
            return {
                "answer": "I don't have enough information to answer this question. Please upload relevant documents first.",
                "confidence": 0.0,
                "sources": [],
                "question": request.question
            }
        
        # 2. Generate answer with LLM
        answer_data = await generate_answer(
            question=request.question,
            context_chunks=search_results,
            model=request.model
        )
        
        # 3. Extract citations
        citations = extract_citations(
            answer=answer_data["answer"],
            sources=search_results
        )
        
        return {
            "answer": answer_data["answer"],
            "confidence": answer_data.get("confidence", 0.8),
            "sources": citations,
            "question": request.question,
            "model": answer_data.get("model", "mistral")
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Question answering failed: {str(e)}")


@router.get("/models")
async def list_available_models():
    """List available Ollama models"""
    try:
        from services.llm.ollama_service import list_models
        models = await list_models()
        return {"models": models}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list models: {str(e)}")
