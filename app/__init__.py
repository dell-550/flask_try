from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml
# 初始化 SQLAlchemy 对象
db = SQLAlchemy()

def create_app( config_path=None):
    app = Flask(__name__)

    # 加载配置
    with open("app/config/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)


    # 更新 Flask 配置
    app.config.update(config)
    db.init_app(app)
    # print(app.config)

    # 注册蓝图或路由
    from app.controller import user_api as user_blueprint
    from app.controller import home_api as home_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user/')
    app.register_blueprint(home_blueprint, url_prefix='/')
    print("app created")
    print(app.url_map)

    return app