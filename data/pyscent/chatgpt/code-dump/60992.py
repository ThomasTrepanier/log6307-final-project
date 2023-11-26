import logging
from flask import Flask
from loguru import logger

app = Flask(__name__)

# Werkzeug logger configuration
werkzeug_logger = logging.getLogger("werkzeug")
werkzeug_logger.addHandler(logging.StreamHandler())
werkzeug_logger.setLevel(logging.DEBUG)

def redirect_werkzeug_logs_to_loguru(record):
    logger_opt = logger.opt(depth=6, exception=record.exc_info)
    logger_opt.log(record.levelno, record.getMessage())

werkzeug_logger.addFilter(redirect_werkzeug_logs_to_loguru)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
