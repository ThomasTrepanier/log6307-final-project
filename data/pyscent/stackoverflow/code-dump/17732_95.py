def deco(f):
    cache = {}
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'r' in kwargs and kwargs['r']:  # reset the cache when first called
            cache.clear()
        try:                                                                                                    
            res = cache[args]  
            # We have already seen these parameters !
            print('cache hit', *args)
            if res is None:
                raise KeyError
        except KeyError:
            cache[args] = None  # temporary store a value here
            res = f(*args)
            cache[args] = res  # final value stored
        return res

    return wrapper
