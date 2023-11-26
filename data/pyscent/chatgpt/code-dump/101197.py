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
