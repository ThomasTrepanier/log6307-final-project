import asyncio
import websockets
from threading import Thread

class Server:
    def __init__(self):
        self.server = None
        self.thread = None
        self.websocket = None

    async def handler(self, websocket, path):
        self.websocket = websocket
        while True:
            try:
                message = await websocket.recv()
                print(f"< Server received: {message}")

                response = "Message received!"
                await websocket.send(response)
                print(f"> Server sent: {response}")
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
        self.server = websockets.serve(self.handler, 'localhost', 8765)
        asyncio.run(self.server)

    def send_message(self, message):
        if self.websocket:
            asyncio.run(self.websocket.send(message))

    def stop(self):
        if self.server:
            self.server.close()
            asyncio.run(self.server.wait_closed())

if __name__ == "__main__":
    server = Server()
    server.start()

    try:
        while True:
            # server is running
            pass
    except KeyboardInterrupt:
        server.stop()
