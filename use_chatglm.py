from langchain_community.chat_models import ChatZhipuAI

def get_llm():
    llm = ChatZhipuAI()
    return llm