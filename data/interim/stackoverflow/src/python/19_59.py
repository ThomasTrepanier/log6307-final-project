import multiprocessing as mp
from multiprocessing import queues


class IterQueue(queues.Queue):

    def __init__(self, *args, **kwargs):
        ctx = mp.get_context()
        kwargs['ctx'] = ctx
        super().__init__(*args, **kwargs)

    # <----  Iter Protocol  ------>
    def __iter__(self):
        return self

    def __next__(self):
        try:
            if not self.empty():
                return self.get()  # block=True | default
            else:
                raise StopIteration
        except ValueError:  # the Queue is closed
            raise StopIteration

