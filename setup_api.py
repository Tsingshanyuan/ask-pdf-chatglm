# 可以修改这个文件来切换不同的API
from use_openai import get_llm
from use_openai import get_embeddings

# 统一接口
def setup_llm():
    llm = get_llm()
    return llm

def setup_embeddings():
    embeddings = get_embeddings()
    return embeddings