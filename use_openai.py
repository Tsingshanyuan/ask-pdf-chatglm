from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings

def get_llm():
    llm = OpenAI()
    return llm

def get_embeddings():
    embeddings = OpenAIEmbeddings()
    return embeddings