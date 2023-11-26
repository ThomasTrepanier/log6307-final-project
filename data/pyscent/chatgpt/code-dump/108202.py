import asyncio
import websockets
from threading import Thread
import logging
import pprint

class Server:
    def __init__(self, on_message=None):
        self.server = None
        self.thread = None
        self.connections = set()
        self.on_message = on_message

        logging.basicConfig(level=logging.INFO)

    async def handler(self, websocket, path):
        remote_ip, remote_port = websocket.remote_address
        logging.info(f"Client connected: {remote_ip}:{remote_port}")
        self.connections.add(websocket)
        try:
            while True:
                try:
                    message = await websocket.recv()
                    if self.on_message:
                        self.on_message(message)
                except websockets.exceptions.ConnectionClosedOK:
                    logging.info("Connection closed normally.")
                    break
                except websockets.exceptions.ConnectionClosedError:
                    logging.info("Connection closed with error.")
                    break
        finally:
            self.connections.remove(websocket)
            logging.info(f"Client disconnected: {remote_ip}:{remote_port}")
            logging.info("Current connections:")
            logging.info(pprint.pformat([str(sock.remote_address) for sock in self.connections]))

    # ...
