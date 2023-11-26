import io
import pandas as pd

# strings in first 3 columns are of arbitrary length
x = '''ABCD,EFGH,IJKL,34.23;562.45;213.5432
MNOP,QRST,UVWX,56.23;63.45;625.234
'''*10**6

def iterstream(iterable, buffer_size=io.DEFAULT_BUFFER_SIZE):
    """
    http://stackoverflow.com/a/20260030/190597 (Mechanical snail)
    Lets you use an iterable (e.g. a generator) that yields bytestrings as a
    read-only input stream.

    The stream implements Python 3's newer I/O API (available in Python 2's io
    module).

    For efficiency, the stream is buffered.
    """
    class IterStream(io.RawIOBase):
        def __init__(self):
            self.leftover = None
        def readable(self):
            return True
        def readinto(self, b):
            try:
                l = len(b)  # We're supposed to return at most this much
                chunk = self.leftover or next(iterable)
                output, self.leftover = chunk[:l], chunk[l:]
                b[:len(output)] = output
                return len(output)
            except StopIteration:
                return 0    # indicate EOF
    return io.BufferedReader(IterStream(), buffer_size=buffer_size)

def replacementgenerator(haystack, needle, replace):
    for s in haystack:
        if s == needle:
            yield str.encode(replace);
        else:
            yield str.encode(s);

csv = pd.read_csv(iterstream(replacementgenerator(x, ";", ",")), usecols=[3, 4, 5])
