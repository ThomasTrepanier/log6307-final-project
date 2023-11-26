from django.core.cache.backends.filebased import FileBasedCache
from django.core.cache.backends.dummy import DummyCache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from constance import config


class MyCache(DummyCache):

    def __init__(self, *args, **kwargs):
        self.dummy_cache = DummyCache(*args, **kwargs)
        self.file_cache = FileBasedCache(*args, **kwargs)

    def _active_cache(self):
        """
        Select either DummyCache or FileBasedCache based on configuration
        """
        return self.file_cache if config.CACHING_ENABLED else self.dummy_cache

    def add(self, key, value, timeout=DEFAULT_TIMEOUT, version=None):
        return self._active_cache().add(key, value, timeout, version)

    def get(self, key, default=None, version=None):
        return self._active_cache().get(key, default, version)

    def set(self, key, value, timeout=DEFAULT_TIMEOUT, version=None):
        self._active_cache().set(key, value, timeout, version)

    def touch(self, key, timeout=DEFAULT_TIMEOUT, version=None):
        return self._active_cache().touch(key, timeout, version)

    def delete(self, key, version=None):
        self._active_cache().delete(key, version)

    def has_key(self, key, version=None):
        return self._active_cache().has_key(key, version)

    def clear(self):
        self._active_cache().clear()
