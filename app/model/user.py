# from db import db
from app import db

class User(db.Model):
    __tablename__ = 'users'  # 表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    username = db.Column(db.String(80), unique=True, nullable=False)  # 用户名
    email = db.Column(db.String(120), unique=True, nullable=False)  # 邮箱
    password = db.Column(db.String(128), nullable=False)  # 密码

    def __repr__(self):
        return f"<User {self.username}>"
    
    def add_user(self, user_data):
        self.username = user_data['username']
        self.password = user_data['password']
        self.email = user_data['email']
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def update_user(self):
        db.session.commit()
    
    def get_user_by_id(self, id):
        return User.query.get(id)
    
    


# db.create_all()