from langchain_community.chat_models import ChatZhipuAI
from zhipuai_embedding import ZhipuAIEmbeddings

def get_llm():
    llm = ChatZhipuAI()
    return llm

def get_embeddings():
    embeddings = ZhipuAIEmbeddings()
    return embeddings