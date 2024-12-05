
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml


handler = RotatingFileHandler('./logs/flask.log', maxBytes=10000, backupCount=1)
handler.setLevel("DEBUG")

# dictConfig({
#         "version": 1,
#         "disable_existing_loggers": False,  # 不覆盖默认配置
#         "formatters": {  # 日志输出样式
#             "default": {
#                 "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#             }
#         },
#         "handlers": {
#             "console": {
#                 "class": "logging.StreamHandler",  # 控制台输出
#                 "level": "DEBUG",
#                 "formatter": "default",
#             },
#             "log_file": {
#                 "class": "logging.handlers.RotatingFileHandler",
#                 "level": "INFO",
#                 "formatter": "default",   # 日志输出样式对应formatters
#                 "filename": "./logs/flask.log",  # 指定log文件目录
#                 "maxBytes": 20*1024*1024,   # 文件最大20M
#                 "backupCount": 10,          # 最多10个文件
#                 "encoding": "utf8",         # 文件编码
#             },

#         },
#         "root": {
#             "level": "DEBUG",  # # handler中的level会覆盖掉这里的level
#             "handlers": ["console", "log_file"],
#         },
#     }
# )


# 初始化 SQLAlchemy 对象
db = SQLAlchemy()

def create_app( config_path=None):
    app = Flask(__name__)
    app.logger.addHandler(handler)
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