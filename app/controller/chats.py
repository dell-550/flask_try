from flask import jsonify, request

from . import chat_api
# from chain.agent import Agent
from app.service import chat_service


    
    


@chat_api.route('/', methods=['POST'])
def chat_message():
    data = request.json
    # print(data)
    res = chat_service.chat_with_agent(data.get('message'))
    # data.message = res.content
    return res
