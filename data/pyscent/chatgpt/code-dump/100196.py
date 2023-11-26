if __name__ == "__main__":
    def on_message(message):
        print(f"Server received: {message}")

    server = Server(on_message)
    server.start()

    try:
        while True:
            message = input("Enter message to send: ")
            server.send_message(message)
    except KeyboardInterrupt:
        server.stop()
