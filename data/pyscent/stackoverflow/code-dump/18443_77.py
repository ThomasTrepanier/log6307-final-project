
import os
import google.cloud.logging
import logging


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    # Instantiates a client
    client = google.cloud.logging.Client()

    # Connects the logger to the root logging handler; by default this captures
    # all logs at INFO level and higher
    client.setup_logging()

    # The data to log
    text = 'Hello, these are logs from cloud run!'

    # Emits the data using the standard logging module
    logging.warning(text)
    return 'Hello {}!\n'.format(text)
