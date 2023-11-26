#!/usr/bin/env python

from os import path as environ

import click

from flask import Flask
from flask.cli import FlaskGroup

def create_app():
    app = Flask(__name__)
    ...
    return app


@click.group(cls=FlaskGroup, create_app=create_app)
@click.option('-e', '--env', default="development")
def manager(env):
    environ["FLASK_ENV"] = env


if __name__ == "__main__":
    manager()
