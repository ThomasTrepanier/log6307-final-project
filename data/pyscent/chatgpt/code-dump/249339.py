import paramiko

def run_ssh_command(hostname, username, password, command):
    # Create SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the SSH server
        client.connect(hostname, username=username, password=password)

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # Monitor command output
        for line in stdout:
            print(line.strip())  # Process the output as needed

        # Check for any errors
        exit_status = stdout.channel.recv_exit_status()
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
command = "ls -l"

run_ssh_command(hostname, username, password, command)
