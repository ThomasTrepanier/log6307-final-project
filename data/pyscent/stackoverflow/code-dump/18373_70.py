import logging as log
import google.cloud.logging as logging

def doSomething(param):
    logging_client = logging.Client()
    logging_client.setup_logging()
log.info(f"Some log here: {param}") 
