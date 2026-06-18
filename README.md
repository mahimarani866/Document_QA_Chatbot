# Document Q&A Chatbot using LLM

A modular Python RAG application for asking questions over uploaded documents. It loads documents, splits them into chunks, retrieves the most relevant context, and answers using an LLM when configured.

## Features

- Upload or index `.txt`, `.md`, `.pdf`, and `.docx` documents.
- Chunk documents with overlap for better retrieval.
- Retrieve relevant passages with a lightweight local vector store.
- Generate grounded answers with OpenAI when `OPENAI_API_KEY` is set.
- Fall back to extractive answers when no LLM key is configured.
- Run through either a Streamlit UI or a CLI.

## Project Structure

```text
.
|-- app.py                  # Streamlit application
|-- rag/
|   |-- document_loader.py  # File parsing
|   |-- text_splitter.py    # Chunking
|   |-- vector_store.py     # Local retrieval
|   |-- llm.py              # LLM and fallback answer generation
|   `-- pipeline.py         # End-to-end RAG orchestration
|-- tests/                  # Focused workflow tests
`-- requirements.txt
```

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Optional LLM setup:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_MODEL="gpt-4o-mini"
```

## Run the App

```powershell
streamlit run app.py
```

## Run from CLI

```powershell
python -m rag.cli --docs path\to\docs --question "What is this document about?"
```

## Test

```powershell
pytest
```

## Resume Summary

**Document Q&A Chatbot using LLM (GenAI + RAG)**  
Designed and implemented a modular document-based Q&A system using Python, retrieval-augmented generation, and LLM integration. Built document ingestion, chunking, semantic-style retrieval, prompt construction, and answer generation workflows, with testing and troubleshooting to improve reliability and maintainability.
