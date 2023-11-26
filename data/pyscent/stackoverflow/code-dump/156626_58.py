@os_dispatch  # fallback in case OS is not supported
def my_callback():
    print('OS not supported')

@my_callback.register('linux')
def _():
    print('Doing something @ Linux')

@my_callback.register('windows')
def _():
    print('Doing something @ Windows')

my_callback()  # dispatches on sys.platform
