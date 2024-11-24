import click
from flask import Flask
from flask.cli import AppGroup


app = Flask(__name__)
# user_cli = AppGroup("user")

@app.cli.command()
@click.argument("name")
def print_user(name):
    print("this is", name)

# app.cli.add_command(user_cli)
