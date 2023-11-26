from queue import PriorityQueue

class CompareError(ValueError): pass

class O:
    def __init__(self,n):
        self.n = n

    def __lq__(self):
        raise CompareError

    def __repr__(self): return str(self)
    def __str__(self): return self.n

def add(prioqueue,prio,item):
    """Adds the 'item' with 'prio' to the 'priorqueue' adding a unique value that
    is stored as member of this method 'add.n' which is incremented on each usage."""
    prioqueue.put( (prio, add.n, item))
    add.n += 1

# no len() on PrioQueue - we ensure our unique integer via method-param
# if you forget to declare this, you get an AttributeError
add.n = 0

h = PriorityQueue()

add(h, 7, O('release product'))
add(h, 1, O('write spec 3'))
add(h, 1, O('write spec 2'))
add(h, 1, O('write spec 1'))
add(h, 3, O('create tests'))

for _ in range(4):
    item = h.get()
    print(item)
