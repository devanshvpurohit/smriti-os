"""
Ollama LLM Service
Local LLM inference using Ollama
"""

import httpx
from typing import List, Dict, Optional
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(backend_dir))

from config import settings


async def check_ollama_connection() -> bool:
    """Check if Ollama is running"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.ollama_base_url}/api/tags", timeout=5.0)
            return response.status_code == 200
    except Exception as e:
        print(f"❌ Ollama connection failed: {e}")
        return False


async def list_models() -> List[Dict]:
    """List available Ollama models"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.ollama_base_url}/api/tags")
            response.raise_for_status()
            data = response.json()
            return data.get("models", [])
    except Exception as e:
        print(f"❌ Failed to list models: {e}")
        return []


async def generate_answer(
    question: str,
    context_chunks: List[Dict],
    model: Optional[str] = None
) -> Dict:
    """
    Generate answer using Ollama with RAG context
    
    Args:
        question: User's question
        context_chunks: Retrieved document chunks
        model: Ollama model name (default from settings)
    
    Returns:
        Dict with answer and metadata
    """
    model_name = model or settings.default_model
    
    # Build context from chunks
    context = "\n\n".join([
        f"[Source: {chunk['filename']}, Page {chunk.get('page_number', 'N/A')}]\n{chunk['content']}"
        for chunk in context_chunks
    ])
    
    # Build prompt
    prompt = f"""You are a helpful AI assistant that answers questions based on provided documents.

Context from documents:
{context}

Question: {question}

Instructions:
- Answer the question using ONLY the information from the provided context
- If the context doesn't contain enough information, say "I don't have enough information to answer this question"
- Include specific references to sources when possible
- Be concise and accurate
- Do not make up information

Answer:"""
    
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{settings.ollama_base_url}/api/generate",
                json={
                    "model": model_name,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "top_p": 0.9,
                    }
                }
            )
            response.raise_for_status()
            data = response.json()
            
            return {
                "answer": data.get("response", "").strip(),
                "model": model_name,
                "confidence": 0.8  # TODO: Implement confidence scoring
            }
    
    except Exception as e:
        print(f"❌ Answer generation failed: {e}")
        return {
            "answer": f"Error generating answer: {str(e)}",
            "model": model_name,
            "confidence": 0.0
        }


async def generate_embedding(text: str) -> List[float]:
    """
    Generate embedding for text using Ollama
    Note: This is a placeholder. In production, use sentence-transformers
    """
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{settings.ollama_base_url}/api/embeddings",
                json={
                    "model": settings.default_embedding_model,
                    "prompt": text
                }
            )
            response.raise_for_status()
            data = response.json()
            return data.get("embedding", [])
    
    except Exception as e:
        print(f"❌ Embedding generation failed: {e}")
        return []
