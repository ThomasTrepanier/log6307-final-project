class cache_last(collections.abc.Iterator):
    """
    Wraps an iterable in an iterator that can retrieve the last value.

    .. attribute:: obj

       A reference to the wrapped iterable. Provided for convenience
       of one-line initializations.
    """
    def __init__(self, iterable):
        self.obj = iterable
        self._iter = iter(iterable)
        self._sentinel = object()

    @property
    def last(self):
        """
        The last object yielded by the wrapped iterator.

        Uninitialized iterators raise a `ValueError`. Exhausted
        iterators raise a `StopIteration`.
        """
        if self.exhausted:
            raise StopIteration
        return self._last

    @property
    def exhausted(self):
        """
        `True` if there are no more elements in the iterator.
        Violates EAFP, but convenient way to check if `last` is valid.
        Raise a `ValueError` if the iterator is not yet started.
        """
        if not hasattr(self, '_last'):
            raise ValueError('Not started!')
        return self._last is self._sentinel

    def __next__(self):
        """
        Retrieve, record, and return the next value of the iteration.
        """
        try:
            self._last = next(self._iter)
        except StopIteration:
            self._last = self._sentinel
            raise
        # An alternative that has fewer lines of code, but checks
        # for the return value one extra time, and loses the underlying
        # StopIteration:
        #self._last = next(self._iter, self._sentinel)
        #if self._last is self._sentinel:
        #    raise StopIteration
        return self._last

    def __iter__(self):
        """
        This object is already an iterator.
        """
        return self
