import socket

IDENTIFIER = "<END_OF_COMMAND_RESULT>"

def send_command(client_socket, command):
    """Send command to the client."""
    client_socket.send(command.encode())

if __name__ == "__main__":
    IP = "10.6.6.88"
    PORT = 1337
    socket_address = (IP, PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(socket_address)
        server_socket.listen(5)
        print("listening for incoming connection requests")
        
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print("connection established with ", client_address)
            try:
                while True:
                    command = input("Enter the command: ").strip()
                    if not command:
                        continue
                    send_command(client_socket, command)
                    
                    if command == "stop":
                        break
                    
                    full_command_result = b''
                    while True:
                        chunk = client_socket.recv(1048)
                        if chunk.endswith(IDENTIFIER.encode()):
                            chunk = chunk[:-len(IDENTIFIER)]
                            full_command_result += chunk
                            break
                        full_command_result += chunk
                    
                    print(full_command_result.decode())
            
            except Exception as e:
                print(f"Exception occurred: {e}")
