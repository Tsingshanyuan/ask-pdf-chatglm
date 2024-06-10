# 速度很快，pdf长度有限制
from erniebot_agent.extensions.langchain.llms import ErnieBot
from erniebot_agent.extensions.langchain.embeddings import ErnieEmbeddings

def get_llm():
    llm = ErnieBot()
    return llm

def get_embeddings():
    embeddings = ErnieEmbeddings()
    return embeddings
