from pathlib import Path
from tempfile import TemporaryDirectory

import streamlit as st

from rag.pipeline import RAGPipeline


st.set_page_config(page_title="Document Q&A Chatbot", page_icon="Q&A", layout="wide")

st.title("Document Q&A Chatbot")

uploaded_files = st.sidebar.file_uploader(
    "Upload documents",
    type=["txt", "md", "pdf", "docx"],
    accept_multiple_files=True,
)

top_k = st.sidebar.slider("Retrieved chunks", min_value=1, max_value=8, value=4)
question = st.chat_input("Ask a question about your documents")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question:
    if not uploaded_files:
        st.warning("Upload at least one document before asking a question.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Reading documents and retrieving context..."):
            with TemporaryDirectory() as tmp_dir:
                paths: list[Path] = []
                for uploaded_file in uploaded_files:
                    path = Path(tmp_dir) / uploaded_file.name
                    path.write_bytes(uploaded_file.getvalue())
                    paths.append(path)

                pipeline = RAGPipeline.from_paths(paths)
                result = pipeline.ask(question, top_k=top_k)

        st.markdown(result.answer)

        with st.expander("Sources"):
            for idx, source in enumerate(result.sources, start=1):
                st.markdown(
                    f"**{idx}. {source.metadata.get('source', 'Document')}** "
                    f"(chunk {source.metadata.get('chunk_id', '?')})"
                )
                st.write(source.text)

    st.session_state.messages.append({"role": "assistant", "content": result.answer})
