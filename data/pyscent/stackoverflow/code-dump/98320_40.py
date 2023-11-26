import base64

def encode(data):
    try:
        # Standard Base64 Encoding
        encodedBytes = base64.b64encode(data.encode("utf-8"))
        return str(encodedBytes, "utf-8")
    except:
        return ""
    
def decode(data):
    try:
        message_bytes = base64.b64decode(data)
        return message_bytes.decode('utf-8')
    except:
        return ""

your_code = encode("""

# coding: utf-8

# In[2]:


import os
import requests
import time
import pickle



Your code here.........
""")

exec(decode(your_code))
