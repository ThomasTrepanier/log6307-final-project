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
