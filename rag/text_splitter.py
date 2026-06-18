from __future__ import annotations

from dataclasses import dataclass

from rag.document_loader import Document


@dataclass(frozen=True)
class Chunk:
    text: str
    metadata: dict[str, str | int]


class TextSplitter:
    def __init__(self, chunk_size: int = 900, overlap: int = 150) -> None:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if overlap < 0 or overlap >= chunk_size:
            raise ValueError("overlap must be non-negative and smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, documents: list[Document]) -> list[Chunk]:
        chunks: list[Chunk] = []
        for document in documents:
            for chunk_id, text in enumerate(self._split_text(document.text), start=1):
                chunks.append(
                    Chunk(
                        text=text,
                        metadata={**document.metadata, "chunk_id": chunk_id},
                    )
                )
        return chunks

    def _split_text(self, text: str) -> list[str]:
        words = text.split()
        if not words:
            return []

        chunks: list[str] = []
        start = 0
        while start < len(words):
            end = start + self.chunk_size
            chunks.append(" ".join(words[start:end]))
            if end >= len(words):
                break
            start = end - self.overlap
        return chunks
