import paramiko

def run_ssh_command(hostname, username, password, command):
    # Create SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the SSH server
        client.connect(hostname, username=username, password=password)

        # Execute the command
        session = client.get_transport().open_session()
        session.exec_command(command)

        # Get command output
        while True:
            if session.recv_ready():
                output = session.recv(4096)
                print(output.decode().strip())
            if session.recv_stderr_ready():
                error = session.recv_stderr(4096)
                print(error.decode().strip())
            if session.exit_status_ready():
                break

        # Check for any errors
        exit_status = session.recv_exit_status()
        if exit_status != 0:
            print(f"Command execution failed with exit status: {exit_status}")
            # Handle the failure as needed
        else:
            print("Command execution successful")

    finally:
        # Close the SSH connection
        client.close()

# Example usage
hostname = "example.com"
username = "your_username"
password = "your_password"
command = "cd /path/to/directory; ./run"

run_ssh_command(hostname, username, password, command)
