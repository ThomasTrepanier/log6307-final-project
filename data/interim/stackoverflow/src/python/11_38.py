class Pool:
    def __init__(self, func: Callable, params: list, thread_max = 10):
        self.func = func
        self.params = params
        self.running = 0
        self.finished = []
        self.thread_max = thread_max
        self.threads = []

    def start(self):
        Thread(target=check, args=(0.2)).start()

    def check(self, t_sleep=0.5):
        done = False
        while not done:
            sleep(t_sleep)
            # first check for finished threads
            for t in threads:
                if not t.isAlive():
                    # do something with return value
                    # ...
                    self.threads.remove(t)

            if not len(self.params): # mean there is no more task left to LAUNCH
                done = len(self.threads) # gonna be 0 when every tasks is COMPLETE
                continue # avoid the next part (launching thread)

            # now start some threads if needed
            while len(self.threads) < self.thread_max:
                arg = self.params.pop()
                thread = Thread(target=self.func, args=(arg, ))
                threads.insert(thread)
                thread.start()
