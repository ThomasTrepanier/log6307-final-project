if linux:
    def my_callback(*args, **kwargs):
        print("Doing something @ Linux")
        return

elif windows:
    def my_callback(*args, **kwargs):
        print("Doing something @ Windows")
        return

else:
     raise NotImplementedError("This platform is not supported")
