from pathlib import Path

from rag.pipeline import RAGPipeline


def test_pipeline_retrieves_relevant_context(tmp_path: Path) -> None:
    document = tmp_path / "company_policy.txt"
    document.write_text(
        "Employees can submit reimbursement claims within 30 days of travel. "
        "Claims need receipts and manager approval.",
        encoding="utf-8",
    )

    pipeline = RAGPipeline.from_paths([document], chunk_size=20, overlap=5)
    result = pipeline.ask("When can employees submit reimbursement claims?", top_k=2)

    assert result.sources
    assert "reimbursement" in result.sources[0].text.lower()


def test_pipeline_handles_no_matching_context(tmp_path: Path) -> None:
    document = tmp_path / "notes.txt"
    document.write_text("The launch checklist includes logging and monitoring.", encoding="utf-8")

    pipeline = RAGPipeline.from_paths([document], chunk_size=20, overlap=5)
    result = pipeline.ask("What is the cafeteria menu?", top_k=2)

    assert result.answer
    assert result.sources == []


def test_pipeline_strips_utf8_bom(tmp_path: Path) -> None:
    document = tmp_path / "bom.txt"
    document.write_text("\ufeffRAG retrieves relevant chunks.", encoding="utf-8")

    pipeline = RAGPipeline.from_paths([document], chunk_size=20, overlap=5)
    result = pipeline.ask("What does RAG retrieve?", top_k=1)

    assert result.sources
    assert "\ufeff" not in result.sources[0].text
