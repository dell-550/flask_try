import click
from flask_cors import CORS
from app import create_app, db
from dotenv import load_dotenv



from app.model.user import User
from tests.test_user import TestUser

load_dotenv(verbose=True)
app = create_app("development")
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": ["Content-Type"]}})


@app.cli.command('init-db')
@click.option('--init-db',  default=True,
              help='create all tables')
def init_db(init_db):
    print(init_db)
    if init_db:
        with app.app_context():
            # 创建所有定义的表
            db.create_all()
            app.logger.info("Database tables created successfully!")

    else:
        app.logger.info("init-db is not set")
    



@app.cli.command()
# @click.option('--test', help='test model')
# help: 'Test model names  Eg:  flask --app .\manage.py test-model tests.test_user' 
@click.argument('test_names', nargs=-1)
def test_model(test_names):
    app.logger.info("test model")
    # print(f"test_names {test_names}")
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    # print(f"tests {tests}")
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,               # SQLAlchemy 数据库实例
        User=User,           # User 模型
        # Follow=Follow,       # Follow 模型
        # Role=Role,           # Role 模型
        # Permission=Permission,  # Permission 模型
        # Post=Post,           # Post 模型
        # Comment=Comment      # Comment 模型
    )



if __name__ == "__main__":
    # with app.app_context():
    #     # 创建所有定义的表
    #     db.create_all()
    #     print("Database tables created successfully!")
    app.run(host='0.0.0.0')
