# 速度很快，不用翻墙，pdf可以很大，但是很贵，消耗的token很多
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings

def get_llm():
    llm = OpenAI()
    return llm

def get_embeddings():
    embeddings = OpenAIEmbeddings()
    return embeddings