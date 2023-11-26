import asyncio
import websockets
from threading import Thread

class Client:
    def __init__(self):
        self.client = None
        self.thread = None
        self.websocket = None

    async def handler(self):
        try:
            async with websockets.connect('ws://localhost:8765') as websocket:
                self.websocket = websocket
                message = "Hello, Server!"
                await websocket.send(message)
                print(f"> Client sent: {message}")

                response = await websocket.recv()
                print(f"< Client received: {response}")
        except websockets.exceptions.ConnectionClosedOK:
            print("Connection closed normally.")
        except websockets.exceptions.ConnectionClosedError:
            print("Connection closed with error.")

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
    client = Client()
    client.start()

    try:
        while True:
            # client is running
            pass
    except KeyboardInterrupt:
        client.stop()
