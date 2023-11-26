import asyncio
import websockets
from threading import Thread
import time

class Client:
    def __init__(self, on_message=None, max_retries=3, retry_interval=5):
        self.client = None
        self.thread = None
        self.websocket = None
        self.on_message = on_message
        self.max_retries = max_retries
        self.retry_interval = retry_interval

    async def handler(self):
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                self.websocket = await websockets.connect('ws://localhost:8765')
                while True:
                    response = await self.websocket.recv()
                    if self.on_message:
                        self.on_message(response)
            except websockets.exceptions.ConnectionClosedOK:
                print("Connection closed normally.")
                self.websocket = None
            except websockets.exceptions.ConnectionClosedError:
                print("Connection closed with error.")
                self.websocket = None
            except OSError:
                print("Failed to connect. Retrying...")
                retry_count += 1
                time.sleep(self.retry_interval)

    def start(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        asyncio.run(self.handler())

    def send_message(self, message):
        if self.websocket:
            asyncio.run(self.websocket.send(message))

    def stop(self):
        if self.client:
            self.client.close()
            asyncio.run(self.client.wait_closed())

if __name__ == "__main__":
    def on_message(message):
        print(f"Client received: {message}")

    client = Client(on_message)
    client.start()

    try:
        while True:
            message = input("Enter message to send: ")
            client.send_message(message)
    except KeyboardInterrupt:
        client.stop()
