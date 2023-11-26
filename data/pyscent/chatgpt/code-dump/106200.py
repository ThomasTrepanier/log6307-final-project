class Server:
    # ...

    async def handler(self, websocket, path):
        self.connections.add(websocket)
        try:
            while True:
                try:
                    message = await websocket.recv()
                    if self.on_message:
                        self.on_message(message)
                except (websockets.exceptions.ConnectionClosedOK, websockets.exceptions.ConnectionClosedError) as e:
                    print(f"Connection closed: {e}")
                    break
                except websockets.exceptions.PayloadTooBig:
                    print("Received message too large. Closing connection.")
                    await websocket.close(code=1009)
                    break
                except websockets.exceptions.InvalidMessage:
                    print("Received invalid message. Closing connection.")
                    await websocket.close(code=1007)
                    break
        finally:
            self.connections.remove(websocket)
    
    # ...
