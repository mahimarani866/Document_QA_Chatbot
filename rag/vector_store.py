from __future__ import annotations

import hashlib
import math
import re
from collections import Counter
from dataclasses import dataclass

from rag.text_splitter import Chunk

TOKEN_RE = re.compile(r"[a-zA-Z0-9]+")


@dataclass(frozen=True)
class SearchResult:
    chunk: Chunk
    score: float


class HashingVectorStore:
    def __init__(self, dimensions: int = 2048) -> None:
        self.dimensions = dimensions
        self._chunks: list[Chunk] = []
        self._vectors: list[dict[int, float]] = []

    def add(self, chunks: list[Chunk]) -> None:
        for chunk in chunks:
            self._chunks.append(chunk)
            self._vectors.append(self._embed(chunk.text))

    def search(self, query: str, top_k: int = 4) -> list[SearchResult]:
        query_vector = self._embed(query)
        scored = [
            SearchResult(chunk=chunk, score=_cosine(query_vector, vector))
            for chunk, vector in zip(self._chunks, self._vectors)
        ]
        return sorted(scored, key=lambda result: result.score, reverse=True)[:top_k]

    def _embed(self, text: str) -> dict[int, float]:
        tokens = TOKEN_RE.findall(text.lower())
        counts: Counter[int] = Counter(_stable_hash(token, self.dimensions) for token in tokens)
        if not counts:
            return {}

        norm = math.sqrt(sum(value * value for value in counts.values()))
        return {index: value / norm for index, value in counts.items()}


def _stable_hash(token: str, dimensions: int) -> int:
    digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
    return int(digest, 16) % dimensions


def _cosine(left: dict[int, float], right: dict[int, float]) -> float:
    if not left or not right:
        return 0.0

    if len(left) > len(right):
        left, right = right, left

    return sum(value * right.get(index, 0.0) for index, value in left.items())
