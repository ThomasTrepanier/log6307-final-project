from flask import Flask
import os

def get_app_base_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_instance_folder_path():
    return os.path.join(get_app_base_path(), 
                        'instance')

app = Flask(__name__,
            instance_path=get_instance_folder_path(),
            instance_relative_config=True)

app.config.from_pyfile('flask.cfg', silent=True)

@app.route('/')
def home():
    return 'Hello World'
