from __future__ import annotations

import argparse
from pathlib import Path

from rag.pipeline import RAGPipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask questions over a folder of documents.")
    parser.add_argument("--docs", required=True, help="Document file or folder path")
    parser.add_argument("--question", required=True, help="Question to ask")
    parser.add_argument("--top-k", type=int, default=4, help="Number of chunks to retrieve")
    args = parser.parse_args()

    doc_path = Path(args.docs)
    paths = _collect_paths(doc_path)
    pipeline = RAGPipeline.from_paths(paths)
    result = pipeline.ask(args.question, top_k=args.top_k)

    print(result.answer)
    if result.sources:
        print("\nSources:")
        for source in result.sources:
            print(f"- {source.metadata.get('source')} chunk {source.metadata.get('chunk_id')}")


def _collect_paths(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if not path.is_dir():
        raise FileNotFoundError(path)

    supported = {".txt", ".md", ".pdf", ".docx"}
    paths = [child for child in path.rglob("*") if child.suffix.lower() in supported]
    if not paths:
        raise FileNotFoundError(f"No supported documents found in {path}")
    return paths


if __name__ == "__main__":
    main()
