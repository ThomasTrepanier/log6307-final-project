import asyncio
import websockets
from threading import Thread

class Server:
    def __init__(self, on_message=None):
        self.server = None
        self.thread = None
        self.websocket = None
        self.on_message = on_message

    async def handler(self, websocket, path):
        self.websocket = websocket
        while True:
            try:
                message = await websocket.recv()
                if self.on_message:
                    self.on_message(message)
            except websockets.exceptions.ConnectionClosedOK:
                print("Connection closed normally.")
                break
            except websockets.exceptions.ConnectionClosedError:
                print("Connection closed with error.")
                break

    def start(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        asyncio.run(self.start_server())

    async def start_server(self):
        async with websockets.serve(self.handler, 'localhost', 8765):
            await asyncio.Future()  # runs forever

    def send_message(self, message):
        if self.websocket:
            asyncio.run(self.websocket.send(message))

    def stop(self):
        if self.server:
            self.server.close()
            asyncio.run(self.server.wait_closed())

if __name__ == "__main__":
    def on_message(message):
        print(f"Server received: {message}")

    server = Server(on_message)
    server.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop()
