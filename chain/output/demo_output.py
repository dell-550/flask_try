# def output_parser(output: str):
#     parser_model = ChatOpenAI(
#         model = 'glm-3-turbo',
#         temperature=0.8,
#         openai_api_base = "https://open.bigmodel.cn/api/paas/v4/"
#     )
#     message = "你需要将传入的文本改写，尽可能更自然。这是你需要改写的文本:`{text}`"
#     return parser_model.invoke(message.format(text=output))
from chain.model.dome_model import ChatModel

class OutputParser:
    
    def __init__(self, message):
        self.parser = ChatModel(model="glm-4-flash",
                            openai_api_base="https://open.bigmodel.cn/api/paas/v4/")  

        self.parser_format = message + ":`{text}`"  
    
    def set_parser(self, message):
         
        self.parser_format = message + ":`{text}`"
    
    def get_parser(self, output: str):
        return self.parser.get_model().invoke(self.parser_format.format(text=output))
    