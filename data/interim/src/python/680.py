import socket
import random
import string

def generate_password(length):
    # Generate a random password of the specified length
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def start_custom_server(port, password_length):
    # Get the local IP address
    ip = socket.gethostbyname(socket.gethostname())

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Generate a random password
    password = generate_password(password_length)

    try:
        # Bind the socket to the local IP address and port
        server_socket.bind((ip, port))

        # Start listening for incoming connections
        server_socket.listen(1)
        print(f"Server is up and running on {ip}:{port}")
        print(f"Password: {password}")

        while True:
            # Wait for a client to connect
            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr[0]}:{addr[1]}")

            # Request password from the client
            client_socket.send("Please enter the password: ".encode())
            entered_password = client_socket.recv(1024).decode()

            # Check if the entered password is correct
            if entered_password == password:
                client_socket.send("Password accepted. Welcome!".encode())
                # Handle the client connection (you can implement your own logic here)
                # For example, you can receive data from the client:
                data = client_socket.recv(1024)
                print(f"Received data: {data.decode()}")
            else:
                client_socket.send("Incorrect password. Connection closed.".encode())

            # Close the client connection
            client_socket.close()

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        # Close the server socket
        server_socket.close()
