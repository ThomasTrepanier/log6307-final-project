@os_dispatch
def my_callback():
    print('OS not supported')

@my_callback.register
def linux():
    print('Doing something @ Linux')

@my_callback.register
def windows():
    print('Doing something @ Windows')
