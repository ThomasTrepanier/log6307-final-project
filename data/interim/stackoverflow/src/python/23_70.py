from collections import deque

def return_last_line(filepath):
    with open(filepath,'r') as f:
        q = deque(f, 1)
    return q[0]
