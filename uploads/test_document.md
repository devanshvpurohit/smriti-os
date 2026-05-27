# Smriti: Private AI for your documents

Smriti is a local-first AI knowledge operating system. It allows you to upload your documents and interact with them using a private AI.

## Key Features
- Local-first: All data stays on your machine.
- Privacy-first: No data is sent to the cloud.
- Desktop-style UI: Familiar multi-window environment.
- RAG Pipeline: Intelligent document retrieval and question answering.
- Citation Engine: Every answer comes with sources.

## How it works
1. Upload your documents (PDF, DOCX, TXT, MD, etc.)
2. Smriti parses and chunks the text.
3. It generates embeddings locally using sentence-transformers.
4. Chunks are stored in ChromaDB vector store.
5. When you ask a question, it retrieves the most relevant chunks.
6. Ollama generates an answer based on the retrieved context.
