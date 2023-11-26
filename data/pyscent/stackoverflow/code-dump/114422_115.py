def composed_shifts(n):
    """Return a function of `n` circular shifts."""
    def f(x):    
        return ft.partial(mit.circular_shifts(x).__getitem__, n)()
    return f
