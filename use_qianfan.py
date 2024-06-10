import os
from langchain_community.embeddings import QianfanEmbeddingsEndpoint

def get_embeddings():
    embeddings = QianfanEmbeddingsEndpoint(
        qianfan_ak=os.environ["QIANFAN_AK"],
        qianfan_sk=os.environ["QIANFAN_SK"]
    )
    return embeddings