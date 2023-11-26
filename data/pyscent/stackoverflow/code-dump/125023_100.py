import hashlib
from pathlib import Path
from time import perf_counter

def sha256sum(filename):
    ''' source:  https://stackoverflow.com/a/44873382/13608599 '''
    h  = hashlib.sha256()
    b  = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def csv_hashes(dir_name):
    ''' Map CSV filenames to SHA hashes. '''
    return { csv_file: sha256sum(csv_file)
             for csv_file in dir_name.rglob('*.csv') }
