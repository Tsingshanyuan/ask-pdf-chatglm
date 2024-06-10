# 速度很快，pdf长度有限制
from langchain_community.embeddings import QianfanEmbeddingsEndpoint

def get_embeddings():
    embeddings = QianfanEmbeddingsEndpoint()
    return embeddings