from app.model import user as user_model

def hello():
    print("hello world")
    return "hello world"


def add_user(data):

    user_model.User().add_user(data)
    return "add user finished" 