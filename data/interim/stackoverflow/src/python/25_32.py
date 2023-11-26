_sentinel = []

def foo(bar: List[int]=_sentinel):
    bar = [] if bar is _sentinel else bar
    return sorted(bar)
