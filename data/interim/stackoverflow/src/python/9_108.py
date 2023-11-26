class SharedIterator:
    """Share the state of an iterator with subclasses."""
    _gen = infinite_stream()
    data = None

    @staticmethod
    def modify():
        """Advance the shared iterator + assign new data."""
        cls = SharedIterator
        cls.data = next(cls._gen)
