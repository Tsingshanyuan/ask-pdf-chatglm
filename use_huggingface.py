from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    embedModelName = "BAAI/bge-large-zh-v1.5"
    embeddings = HuggingFaceEmbeddings(model_name=embedModelName)
    return embeddings