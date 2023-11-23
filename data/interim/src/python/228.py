class Server:
    def __init__(self, on_message=None):
        self.server = None
        self.thread = None
        self.connections = set()
        self.on_message = on_message

    async def handler(self, websocket, path):
        self.connections.add(websocket)
        try:
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
        finally:
            self.connections.remove(websocket)

    def send_message(self, message):
        for connection in self.connections:
            asyncio.run(connection.send(message))
