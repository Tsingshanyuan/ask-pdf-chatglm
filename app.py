from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from setup_api import setup_llm, setup_embeddings


def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")
    
    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    # extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # split into chunks
        text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
        chunks = text_splitter.split_text(text)
        
        # create embeddings
        embeddings =  setup_embeddings() # 统一接口
        knowledge_base = FAISS.from_texts(chunks, embeddings)

    # 用于跟踪对话历史
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        
    messages = st.container()

    # 显示用户输入和回答
    user_question = st.chat_input("Ask a question about your PDF:")
    
    if user_question:  # 确保用户输入了问题
        # 加载LLM和QA链
        llm = setup_llm() # 统一接口
        chain = load_qa_chain(llm, chain_type="stuff")
        
        # 将用户输入添加到对话历史中
        st.session_state.messages.append({"role": "user", "text": user_question})
        
        docs = knowledge_base.similarity_search(user_question)
        
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
        if response is not None:
            # 将LLM的回答添加到对话历史中
            st.session_state.messages.append({"role": "assistant", "text": response})

    # 显示对话历史
    for message in st.session_state.messages:
        if message["role"] == "user":
            messages.chat_message("user").write(message["text"])
        elif message["role"] == "assistant":
            messages.chat_message("assistant").write(message["text"])
    

if __name__ == '__main__':
    main()
