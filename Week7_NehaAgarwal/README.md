 Week 7 - Document Question Answering System (RAG)


This project is a Retrieval-Augmented Generation (RAG) application that allows users to upload a PDF document and ask questions based on its content.

Technologies Used
- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- Google Gemini API

Features
- Upload any PDF
- Semantic document search
- AI-generated answers using Gemini
- Interactive Streamlit web interface

 Project Structure

```
Week7_NehaAgarwal/
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

How to Run

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Create a folder named `Documents` and place your PDF inside it (or use the app's upload feature, depending on your implementation).

3. Run the application:

```bash
streamlit run app.py
```
