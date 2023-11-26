import base64

your_code = base64.b64encode(b"""

# All your code goes in here.  

import socket 
import threading
import pickle

class Server :
    def __init__(self) :
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER =  socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
# Continue your code...
""")

exec(base64.b64decode(your_code))
