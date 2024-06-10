# 速度很快，pdf长度有限制
from langchain_community.embeddings import BaichuanTextEmbeddings

def get_embeddings():
    embeddings =  BaichuanTextEmbeddings()
    return embeddings