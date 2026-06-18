from __future__ import annotations

import os

from rag.text_splitter import Chunk


SYSTEM_PROMPT = (
    "You are a document Q&A assistant. Answer only from the provided context. "
    "If the context does not contain the answer, say that the documents do not provide enough information."
)


class AnswerGenerator:
    def __init__(self, model: str | None = None) -> None:
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def answer(self, question: str, chunks: list[Chunk]) -> str:
        if os.getenv("OPENAI_API_KEY"):
            try:
                return self._openai_answer(question, chunks)
            except Exception as exc:
                return (
                    "I could not complete the LLM call, so here is the most relevant "
                    f"context I found instead.\n\n{self._extractive_answer(chunks)}\n\nError: {exc}"
                )

        return self._extractive_answer(chunks)

    def _openai_answer(self, question: str, chunks: list[Chunk]) -> str:
        from openai import OpenAI

        context = "\n\n".join(
            f"Source: {chunk.metadata.get('source')} | Chunk: {chunk.metadata.get('chunk_id')}\n{chunk.text}"
            for chunk in chunks
        )

        client = OpenAI()
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Context:\n{context}\n\nQuestion: {question}",
                },
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content or ""

    def _extractive_answer(self, chunks: list[Chunk]) -> str:
        if not chunks:
            return "The documents do not provide enough information to answer that question."

        context = "\n\n".join(
            f"- {chunk.text}\n  Source: {chunk.metadata.get('source')}, chunk {chunk.metadata.get('chunk_id')}"
            for chunk in chunks
        )
        return (
            "LLM credentials are not configured, so I found the most relevant passages instead:\n\n"
            f"{context}"
        )
