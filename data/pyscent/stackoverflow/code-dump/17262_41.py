import mmap
from time import perf_counter as pf
def load_files(filelist):
    start = pf() # for rough time calculations
    for filename in filelist:
        with open(filename, mode="r", encoding="utf8") as file_obj:
            with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_file_obj:
                data = pickle.load(mmap_file_obj)
                print(data)
    print(f'Operation took {pf()-start} sec(s)')
