class Client:
    # ...

    async def handler(self):
        self.websocket = await websockets.connect('ws://localhost:8765')
        try:
            message = "Hello, Server!"
            await self.websocket.send(message)
            print(f"> Client sent: {message}")

            while True:
                response = await self.websocket.recv()
                print(f"< Client received: {response}")
        except websockets.exceptions.ConnectionClosedOK:
            print("Connection closed normally.")
            self.websocket = None
        except websockets.exceptions.ConnectionClosedError:
            print("Connection closed with error.")
            self.websocket = None

    # ...
