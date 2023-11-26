class Particle:

    # better to make this an implementation attribute
    _ID = 0

    @classmethod
    def _next_id(cls):
        cls._ID += 1
        return cls._ID

    def __init__(self, rect):
        self.ID = self._next_id()
        self.color = (255, 0, 0)
