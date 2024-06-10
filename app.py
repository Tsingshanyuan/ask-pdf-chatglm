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

      
      # 检查 Session State 是否有对话历史记录
      if 'conversation_history' not in st.session_state:
          st.session_state.conversation_history = []

      # 初始化迭代计数器
      if 'iteration_count' not in st.session_state:
          st.session_state.iteration_count = 0

      # 显示用户输入和回答
      while True:
          # 为每次循环迭代生成一个唯一的 key
          unique_key = f'user_question_{st.session_state.iteration_count}'
          
          user_question = st.text_input("Ask a question about your PDF (type 'exit' to stop):", key=unique_key)
          
          # 如果用户输入了 'exit' 或者输入框为空，则退出循环
          if user_question.strip().lower() == 'exit' or not user_question.strip():
              break
          
          if user_question:  # 确保用户输入了问题
              docs = knowledge_base.similarity_search(user_question)

              llm = setup_llm() # 统一接口
              chain = load_qa_chain(llm, chain_type="stuff")
              with get_openai_callback() as cb:
                  response = chain.run(input_documents=docs, question=user_question)
                  # 存储对话历史
                  st.session_state.conversation_history.append((user_question, response))

              st.write(f"Q: {user_question}")
              st.write(f"A: {response}")
          
          # 更新迭代计数器，为下一次循环准备
          st.session_state.iteration_count += 1

      # 显示对话历史
      st.header("Conversation History")
      for question, answer in st.session_state.conversation_history:
          st.write(f"Q: {question}")
          st.write(f"A: {answer}")
    

if __name__ == '__main__':
    main()
