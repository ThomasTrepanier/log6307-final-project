class Client:
    # ...

    async def handler(self):
        retry_count = 0
        while retry_count < self.max_retries:
            try:
                self.websocket = await websockets.connect('ws://localhost:8765')
                while True:
                    response = await self.websocket.recv()
                    if self.on_message:
                        self.on_message(response)
            except (websockets.exceptions.ConnectionClosedOK, websockets.exceptions.ConnectionClosedError) as e:
                print(f"Connection closed: {e}")
                self.websocket = None
            except websockets.exceptions.PayloadTooBig:
                print("Received message too large. Disconnecting.")
                await self.websocket.close()
                self.websocket = None
                break
            except websockets.exceptions.InvalidMessage:
                print("Received invalid message. Disconnecting.")
                await self.websocket.close()
                self.websocket = None
                break
            except OSError:
                print("Failed to connect. Retrying...")
                retry_count += 1
                time.sleep(self.retry_interval)

    # ...
