def process_up(self):
    try:
        call = subprocess.check_output("pidof '{}'".format(self.processName), shell=True)
        return True
    except subprocess.CalledProcessError:
        return False
