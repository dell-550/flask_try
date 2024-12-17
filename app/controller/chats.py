from flask import jsonify, request

from . import chat_api
# from chain.agent import Agent
from app.service import chat_service


    
    


@chat_api.route('/', methods=['POST'])
def chat_message():

    # return res
    try:
        data = request.json
    # print(data)
        res = chat_service.chat_with_agent(data.get('message'))
        return jsonify({'code': 200,'msg': 'success','reply': res})
    # data.message = res.content
    except:
        return jsonify({'code': 1001, 'msg': '参数错误'})
