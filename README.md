# 🤖 Document Q&A Chatbot

> An intelligent RAG-based chatbot that answers questions from your PDF documents using Google Gemini and LangChain.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C5A?style=for-the-badge&logo=chainlink&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-00897B?style=for-the-badge&logo=meta&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Sentence_Transformers-FF6F00?style=for-the-badge&logo=huggingface&logoColor=white)
![PyPDF](https://img.shields.io/badge/PyPDF-E44D26?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)
![RAG](https://img.shields.io/badge/RAG_Pipeline-6DB33F?style=for-the-badge&logo=databricks&logoColor=white)

---

## 📌 About The Project

A **Retrieval-Augmented Generation (RAG)** based Document Q&A chatbot built as a Final Year Project. Upload any PDF and ask questions — the chatbot answers **only from your document**, not from general AI knowledge.

---

## ✨ Features

- 📤 **PDF Upload** — Upload any PDF document
- 📖 **Text Extraction** — Automatically reads all text from the PDF
- ✂️ **Smart Chunking** — Splits text into meaningful chunks
- 🧠 **Embeddings** — Converts text into vector representations
- 🔍 **FAISS Vector Search** — Finds the most relevant chunks semantically
- 🤖 **Gemini LLM** — Google Gemini generates accurate answers
- 💬 **Chat History** — Full conversational memory
- 📎 **Source References** — Shows which part of the document was used
- 🎨 **Clean Streamlit UI** — Simple and intuitive interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web UI framework |
| LangChain | LLM orchestration framework |
| Google Gemini API | Large Language Model |
| FAISS | Vector similarity search database |
| Sentence Transformers | Text embedding generation |
| PyPDF | PDF text extraction |
| python-dotenv | Environment variable management |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Document_QA_Chatbot.git
cd Document_QA_Chatbot
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
```bash
cp .env.example .env
```
Open `.env` and add your key:
```
GOOGLE_API_KEY=your_actual_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Document_QA_Chatbot/
├── app.py              # Streamlit UI
├── utils.py            # RAG pipeline logic
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── data/               # Uploaded PDFs (local)
├── vectorstore/        # FAISS index (local)
└── README.md
```

---

## 🔑 Get a Free Gemini API Key

1. Go to https://aistudio.google.com/app/apikey
2. Click **Create API Key**
3. Paste it in your `.env` file

---

## 👩‍💻 Author

**M Mahima Rani**
Final Year Project — Generative AI Application Development
