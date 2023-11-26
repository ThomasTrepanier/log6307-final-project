def read(self, endpoint, size_or_buffer, timeout = None):
    r"""Read data from the endpoint.
    This method is used to receive data from the device. The endpoint
    parameter corresponds to the bEndpointAddress member whose endpoint
    you want to communicate with. The size_or_buffer parameter either
    tells how many bytes you want to read or supplies the buffer to
    receive the data (it *must* be an object of the type array).
    The timeout is specified in miliseconds.
    If the size_or_buffer parameter is the number of bytes to read, the
    method returns an array object with the data read. If the
    size_or_buffer parameter is an array object, it returns the number
    of bytes actually read.
    """
