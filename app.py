import streamlit as st
import tempfile

from rag import get_answer

st.set_page_config(
    page_title="Document Question Answering (RAG)",
    page_icon="📚"
)

st.title("📚 Document Question Answering System")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

question = st.text_input(
    "Ask your Question"
)

if st.button("Get Answer"):

    if uploaded_file is None:
        st.warning("Please upload a PDF.")
    elif question == "":
        st.warning("Please enter a question.")
    else:

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        with st.spinner("Searching document..."):

            answer = get_answer(pdf_path, question)

        st.subheader("Answer")

        st.success(answer)

