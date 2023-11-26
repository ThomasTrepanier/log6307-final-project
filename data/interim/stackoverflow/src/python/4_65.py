from subprocess import PIPE, Popen


def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


token = cmdline("gcloud auth application-default print-access-token")
print("Token:"+token)
