from flask import  jsonify, request

from . import user_api
from app.service import user_service
@user_api.route('/adduser/', methods=['POST'])
def add_user():
    data = request.values
    try:
        assert data['username'] and data['password'] and data['email']
        datas = user_service.add_user(data)
        return jsonify({'code': 200, 'msg': datas})
    except:
        return jsonify({'code': 1001, 'msg': '参数错误'})
    
    


@user_api.route('/', methods=['GET'])
def users():
    data = user_service.hello()

    return data
