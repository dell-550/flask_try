from flask import jsonify, request

from . import home_api
# from app.service import user_service


    
    


@home_api.route('/', methods=['GET'])
def home():
    data = {
        "name": "this is home page "
    }
    return data