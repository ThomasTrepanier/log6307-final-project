import asyncio
import websockets
from threading import Thread
import time
import logging

class Client:
    def __init__(self, on_message=None, max_retries=3, retry_interval=5):
        self.client = None
        self.thread = None
        self.websocket = None
        self.on_message = on_message
        self.max_retries = max_retries
        self.retry_interval = retry_interval

        logging.basicConfig(level=logging.INFO)

    async def handler(self):
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                self.websocket = await websockets.connect('ws://localhost:8765')
                logging.info(f"Connected to server at ws://localhost:8765")
                # ...
