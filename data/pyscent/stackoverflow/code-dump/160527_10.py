from sys import getsizeof
import math
def chunkify_list(L, max_size_kb):
    chunk_size_elements = int(math.ceil(len(L)/int(math.ceil(getsizeof(L)/(1024*max_size_kb)))))
    return [L[x: x+chunk_size_elements] for x in range(0, len(L), chunk_size_elements)]
