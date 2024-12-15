from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model = 'glm-4-flash',
    openai_api_base = "https://open.bigmodel.cn/api/paas/v4/",
)