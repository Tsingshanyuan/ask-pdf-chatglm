from langchain_community.embeddings import QianfanEmbeddingsEndpoint

def get_embeddings():
    embeddings = QianfanEmbeddingsEndpoint()
    return embeddings