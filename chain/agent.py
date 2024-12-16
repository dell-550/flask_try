# from dotenv import load_dotenv
# load_dotenv(verbose=True)

from chain.model.dome_model import ChatModel
from chain.output.demo_output import OutputParser
from chain.prompt.demo_prompt import Prompt

        # self.parser_model = ChatModel
        # self.parser =  self.parser_model.set_model(model="glm-4-flash",
        #                     openai_api_base="https://open.bigmodel.cn/api/paas/v4/")   


prompt = Prompt(system_info="你是一个高级python开发工程师,帮助我解决编程上的问题", user_info="我在使用python时，遇到了这个问题{promble}，请你帮我解决并详细解答")

# prompt.set_prompt()

model = ChatModel(model="glm-4-flash", openai_api_base="https://open.bigmodel.cn/api/paas/v4/")

output_parser = OutputParser(message="你需要将传入的文本改写，尽可能更自然。这是你需要改写的文本")

chains = prompt.get_prompt() | model.get_model() | output_parser.get_parser

res = chains.invoke(input = {'promble': "import 怎么使用"})

print(res.content)

class Agent:
    model = ChatModel(model="glm-4-flash", openai_api_base="https://open.bigmodel.cn/api/paas/v4/")
    prompt =  Prompt(system_info="你是一个高级python开发工程师,帮助我解决编程上的问题", user_info="我在使用python时，遇到了这个问题{promble}，请你帮我解决并详细解答")
    output = OutputParser(message="你需要将传入的文本改写，尽可能更自然。这是你需要改写的文本")

    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    
    def bind_tools(self,):
        pass
    
    def set_model(self,model, openai_api_base):
        self.model = ChatModel(model=model, openai_api_base=openai_api_base)
    
    def set_prompt(self, system_info, user_info):
        self.prompt = Prompt(system_info="你是一个高级python开发工程师,帮助我解决编程上的问题", user_info="我在使用python时，遇到了这个问题{promble}，请你帮我解决并详细解答")
    
    def set_output(self,message):
        self.output = OutputParser(message=message)
    
    def get_agent(self,):
        return prompt.get_prompt() | model.get_model() | output_parser.get_parser
    
