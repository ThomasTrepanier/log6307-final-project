def _defrost(cls):
    cls.stash_setattr = cls.__setattr__
    cls.stash_delattr = cls.__delattr__
    cls.__setattr__ = object.__setattr__
    cls.__delattr__ = object.__delattr__

def _refreeze(cls):
    cls.__setattr__ = cls.stash_setattr
    cls.__delattr__ = cls.stash_delattr
    del cls.stash_setattr
    del cls.stash_delattr

def temp_unfreeze_for_postinit(func):
    assert func.__name__ == '__post_init__'
    def wrapper(self, *args, **kwargs):
        _defrost(self.__class__)
        func(self, *args, **kwargs)
        _refreeze(self.__class__)
    return wrapper
