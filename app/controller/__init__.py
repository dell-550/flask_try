from flask import Blueprint
from flask_cors import CORS

user_api = Blueprint('user', __name__)
home_api = Blueprint('home', __name__)
chat_api = Blueprint('chat', __name__)

from . import homes
from . import users
from . import chats

# CORS(homes)
# CORS(users)
# CORS(chats)