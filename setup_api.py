# 可以修改这个文件来切换不同的API
'''
# 使用openai的API
# 速度很快，不用翻墙，pdf可以很大，但是很贵，消耗的token很多
from use_openai import get_llm
from use_openai import get_embeddings

# 使用chatglm配合huggingface
from use_chatglm import get_llm
# 需要翻墙才能用，需要本地部署huggingface model
from use_huggingface import get_embeddings

# 使用chatglm配合baichuan
# 速度很快，pdf长度有限制
from use_chatglm import get_llm
from use_baichuan import get_embeddings

# 使用ernie文心一言
# 速度很快，pdf长度有限制
from use_ernie import get_llm
from use_ernie import get_embeddings

# 使用chatglm配合qianfan
# 速度很快，pdf长度有限制，我有qianfan的额度
from use_chatglm import get_llm
from use_qianfan import get_embeddings
'''

# 使用chatglm
from use_chatglm import get_llm
from use_chatglm import get_embeddings


# ------------------------------------------------------------------------------
# 统一接口
def setup_llm():
    llm = get_llm()
    return llm

def setup_embeddings():
    embeddings = get_embeddings()
    return embeddings