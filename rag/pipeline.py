from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from rag.document_loader import load_documents
from rag.llm import AnswerGenerator
from rag.text_splitter import Chunk, TextSplitter
from rag.vector_store import HashingVectorStore


@dataclass(frozen=True)
class QAResult:
    answer: str
    sources: list[Chunk]


class RAGPipeline:
    def __init__(self, chunks: list[Chunk], answer_generator: AnswerGenerator | None = None) -> None:
        self.store = HashingVectorStore()
        self.store.add(chunks)
        self.answer_generator = answer_generator or AnswerGenerator()

    @classmethod
    def from_paths(
        cls,
        paths: list[Path],
        chunk_size: int = 900,
        overlap: int = 150,
    ) -> "RAGPipeline":
        documents = load_documents(paths)
        chunks = TextSplitter(chunk_size=chunk_size, overlap=overlap).split(documents)
        return cls(chunks)

    def ask(self, question: str, top_k: int = 4) -> QAResult:
        results = self.store.search(question, top_k=top_k)
        sources = [result.chunk for result in results if result.score > 0]
        answer = self.answer_generator.answer(question, sources)
        return QAResult(answer=answer, sources=sources)
