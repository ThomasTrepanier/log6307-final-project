a = [1, 2, 2, 3, 3, 4, 5, 6]
    
def get_unique_N(iterable, N):
    """Yields (in order) the first N unique elements of iterable. 
    Might yield less if data too short."""
    seen = set()
    for e in iterable:
        if e in seen:
            continue
        seen.add(e)
        yield e
        if len(seen) == N:
            return
            
k = get_unique_N([1, 2, 2, 3, 3, 4, 5, 6], 4)
print(list(k))
    
