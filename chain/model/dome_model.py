from langchain_openai import ChatOpenAI


# model = ChatOpenAI(
#     # temperature=0.95,
#     model="glm-4-flash",
#     # openai_api_key="995979076bb2014a6efb10b2c7e56f54.BkJE79YUK0c8bOJu",
#     openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
# )

class ChatModel:
    def __init__(self, model, openai_api_base):
        self.model = ChatOpenAI(
                # temperature=0.95,
                model=model,
                openai_api_base=openai_api_base
            )

    def set_model(self, model, openai_api_base):
        self.model = ChatOpenAI(
                # temperature=0.95,
                model=model,
                openai_api_base=openai_api_base
            )

    def get_model(self):
        return self.model
    