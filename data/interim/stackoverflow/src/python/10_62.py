class MyContainer(list): # inherits == operator and from list, so empty containers are equal
    def append(self, value):
        super().append(value)

callbacks = []
def register_callback(cb):
    if cb not in callbacks:  # this does an == test against all previously registered callbacks
        callbacks.append(cb)

def do_callbacks(*args):
    for cb in callbacks:
        cb(*args)

container1 = MyContainer()
register_callback(container1.append)
container2 = MyContainer()
register_callback(container2.append)

do_callbacks('foo')

print(container1 == container2)   # this should be true, if both callbacks got run
