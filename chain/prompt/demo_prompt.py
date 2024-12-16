from langchain.prompts import ChatPromptTemplate


# prompt_template = ChatPromptTemplate.from_messages(
#     [
#         ('system', "你被用于抑制用户的购买欲望。当用户说想要买什么东西时，你需要提供理由让用户不要买。"),
#         ('human', "我正在考虑购买一个{product}，但我想抑制这个购买欲望。你能帮我列出一些理由，让我思考一下我是否真的需要这个商品吗？")
#     ]
# )


class Prompt:

    def __init__(self, system_info, user_info):
        self.prompt = ChatPromptTemplate.from_messages(
                [
                    ('system', system_info),
                    ('human', user_info)
                ]
            )
    
    def set_prompt(self, system_info, user_info):
        self.prompt = ChatPromptTemplate.from_messages(
                [
                    ('system', system_info),
                    ('human', user_info)
                ]
            )
    
    def get_prompt(self):
        return self.prompt
