from flask import Blueprint

user_api = Blueprint('user', __name__)
home_api = Blueprint('home', __name__)

from . import homes
from . import users