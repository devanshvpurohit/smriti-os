"""
Citation Service
Extract and format citations from search results
"""

from typing import List, Dict
import re


def extract_citations(answer: str, sources: List[Dict]) -> List[Dict]:
    """
    Extract citations from answer and format them
    
    Args:
        answer: Generated answer text
        sources: List of source chunks used for answer
    
    Returns:
        List of formatted citations
    """
    citations = []
    
    for idx, source in enumerate(sources):
        citation = {
            "id": idx + 1,
            "document_id": source["document_id"],
            "chunk_id": source["chunk_id"],
            "filename": source["filename"],
            "page_number": source.get("page_number"),
            "content_snippet": truncate_text(source["content"], 200),
            "similarity_score": source.get("similarity_score", 0.0),
            "highlighted_text": extract_relevant_snippet(source["content"], answer)
        }
        citations.append(citation)
    
    return citations


def truncate_text(text: str, max_length: int) -> str:
    """Truncate text to max_length characters"""
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + "..."


def extract_relevant_snippet(content: str, answer: str) -> str:
    """
    Extract the most relevant snippet from content based on answer
    TODO: Implement more sophisticated relevance matching
    """
    # Simple approach: find overlapping words
    answer_words = set(answer.lower().split())
    content_words = content.lower().split()
    
    # Find the sentence with most overlapping words
    sentences = content.split('.')
    best_sentence = ""
    max_overlap = 0
    
    for sentence in sentences:
        sentence_words = set(sentence.lower().split())
        overlap = len(answer_words.intersection(sentence_words))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sentence = sentence.strip()
    
    return best_sentence if best_sentence else truncate_text(content, 150)


def format_citation_text(citations: List[Dict]) -> str:
    """
    Format citations as text for display
    """
    if not citations:
        return ""
    
    citation_text = "\n\nSources:\n"
    for citation in citations:
        page_info = f", Page {citation['page_number']}" if citation['page_number'] else ""
        citation_text += f"[{citation['id']}] {citation['filename']}{page_info}\n"
    
    return citation_text