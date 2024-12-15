from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv(verbose=True)
model = ChatOpenAI(
    # temperature=0.95,
    model="glm-4-flash",
    # openai_api_key="995979076bb2014a6efb10b2c7e56f54.BkJE79YUK0c8bOJu",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)



import pandas as pd
from pandasql import sqldf

from langchain.tools import tool


@tool
def simulate_database_operation(sql: str):
	'''根据sql语句操作数据库'''
	my_table = pd.DataFrame({
	    'name': ['Henry Myers', 'Martha Hawkins', 'Kelsey Lutz', 'Jonathan Fowler', 'Jonathan Young', 'Autumn Johnson', 'Kimberly Macias', 'Jared Mccormick', 'Casey Hoover', 'Erica Morse'],
	    'age': [60, 44, 54, 46, 76, 22, 69, 33, 23, 35],
	    'sex': ['F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M']
	})
	result = sqldf(sql)
	return result

# print(simulate_database_operation('SELECT * FROM my_table WHERE age > 50'))

from langchain_community.tools import DuckDuckGoSearchRun

tools = [DuckDuckGoSearchRun(), simulate_database_operation]
model_with_tools = model.bind_tools(tools)

from pprint import pprint as pp

# response = model_with_tools.invoke('印度的首都是哪里？')
# pp(dict(response))

fetch_response = model_with_tools.invoke('现在是北京时间几点？查询之后告诉我')
pp(dict(fetch_response))

db_response = model_with_tools.invoke('帮我往数据库的my_table表中插入一条数据，name是张三，age是18，sex是male')
pp(dict(db_response))

from icecream import ic

def manual_agent(query: str, model: ChatOpenAI, tools:list[tool]):
    model_with_tools = model.bind_tools(tools)
    model_output = model_with_tools.invoke(query)
    tool_response = call_tool(model_output, tools)
    final_response = model.invoke(
        f'original query: {query} \n\n\n tool response: {tool_response}',
    )
    return final_response


def call_tool(model_output, tools):
    tools_map = {tool.name.lower(): tool for tool in tools}
    tools_response = {}
    for tool in model_output.tool_calls:
        tool_name = tool['name']
        tool_args = tool['args']
        tool_instance = tools_map[tool_name]
        tool_response = tool_instance.invoke(*tool_args.values())
        tools_response[tool_name] = tool_response
    return tools_response

manual_agent('帮我查询数据库my_table表中有多少人年龄大于60', model, tools).content

from langgraph.prebuilt import create_react_agent
agent = create_react_agent(model, tools)
from langchain_core.messages import HumanMessage
response = agent.invoke({'messages': [HumanMessage(content="今天在北京的天气怎么样")]})
pp(response)