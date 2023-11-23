import paramiko
import concurrent.futures

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

        # Return the output
        return session.makefile().read()

    finally:
        # Close the SSH connection
        client.close()

# Define your commands
commands = [
    {
        "hostname": "gox",
        "username": "your_username",
        "password": "your_password",
        "command": "sshfs s:/media/s/Elvis/Photo v",
    },
    {
        "hostname": "gox",
        "username": "your_username",
        "password": "your_password",
        "command": "cd src/letz; podman run -v ~/v:/v:ro -v .:/app:exec -p 5000:5000 --rm -it --name pyt py bash -c './yt.sh'",
    },
    {
        "hostname": "gox",
        "username": "your_username",
        "password": "your_password",
        "command": "cd src/letz; podman run -v .:/app:exec -p 8000:8000 --rm -it --name cos1 cos npm run dev -- --port 3000 --host 0.0.0.0",
    },
    # Add more commands as needed
]

# Create a ThreadPoolExecutor with the maximum number of workers
with concurrent.futures.ThreadPoolExecutor(max_workers=len(commands)) as executor:
    # Submit each command to the executor
    future_results = [executor.submit(run_ssh_command, cmd["hostname"], cmd["username"], cmd["password"], cmd["command"]) for cmd in commands]

    # Process the results as they become available
    for future in concurrent.futures.as_completed(future_results):
        result = future.result()
        # Process the result (e.g., display or save the output as needed)
        print(result)
