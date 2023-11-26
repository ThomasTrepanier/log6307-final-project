import pytest

old_skipif = pytest.mark.skipif

def custom_skipif(*args, **kwargs):
    return old_skipif(False, reason='disabling skipif')

pytest.mark.skipif = custom_skipif
