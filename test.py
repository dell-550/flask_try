from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv(verbose=True)
model = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    # openai_api_key="995979076bb2014a6efb10b2c7e56f54.BkJE79YUK0c8bOJu",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)



import pandas as pd
from pandasql import sqldf

def simulate_database_operation(sql):
	my_table = pd.DataFrame({
	    'name': ['Henry Myers', 'Martha Hawkins', 'Kelsey Lutz', 'Jonathan Fowler', 'Jonathan Young', 'Autumn Johnson', 'Kimberly Macias', 'Jared Mccormick', 'Casey Hoover', 'Erica Morse'],
	    'age': [60, 44, 54, 46, 76, 22, 69, 33, 23, 35],
	    'sex': ['F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M']
	})
	result = sqldf(sql)
	return result

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

from langchain_community.tools import DuckDuckGoSearchRun

tools = [DuckDuckGoSearchRun(), simulate_database_operation]
model_with_tools = model.bind_tools(tools)

from pprint import pprint as pp

fetch_response = model_with_tools.invoke('现在是北京时间几点？查询之后告诉我')
pp(dict(fetch_response))