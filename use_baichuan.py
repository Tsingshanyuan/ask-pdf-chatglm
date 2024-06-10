from langchain_community.embeddings import BaichuanTextEmbeddings

def get_embeddings():
    embeddings =  BaichuanTextEmbeddings()
    return embeddings