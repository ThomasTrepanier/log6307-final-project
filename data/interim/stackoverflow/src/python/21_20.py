import threading as th
import time

class CTask(object):

    once  = 1
    loop  = 8

    def __init__(self, foo, args, kwargs, type):
        self.__kwargs = kwargs
        self.__args = args
        self.__foo = foo
        self.__ret = None

        self.task_type = type
        self.terminated = False

    def pool_call(self):
        self.__ret = self.__foo(
            *self.__args,
            **self.__kwargs
        )
        if self.task_type == self.once:
            self.terminated = True

    def __call__(self):
        return self.__ret

    def terminate(self):
        self.terminated = True

class Worker_Pool:

    def push_task(self, type=CTask.once):
        def func_wraper(func):
            def varg_wraper(*a, **b):
                ntask = CTask(func, a, b, type)
                self.__lock.acquire(True, -1)
                self.__ref.append(ntask)
                self.__lock.release()
                return ntask
            return varg_wraper
        return func_wraper

    def __init__(self, n_work):
        self.__lock = th.Lock()
        self.__pool = []
        self.__ref = []
        self.alive = True

        for _ in range(n_work):
            self.__pool.append(
                th.Thread(target=self.__run)
            )
        for w in self.__pool:
            w.start()

    def __run(self):
        while self.alive:
            wtask = None
            if self.__lock.acquire(True, 0.1):
                if len(self.__ref) > 0:
                    wtask = self.__ref.pop(0)
                self.__lock.release()

            if wtask is None or wtask.terminated:
                continue

            wtask.pool_call()

            if wtask.task_type == CTask.loop:
                self.__lock.acquire(True, -1)
                self.__ref.append(wtask)
                self.__lock.release()

    def terminate(self):
        self.alive = False
        for w in self.__pool:
            w.join()

bg = Worker_Pool(3)

class Some_App:

    @bg.push_task(CTask.loop)
    def do_task(self):
        print(f'[{self.id}] -> {self.num}')
        time.sleep(0.5)

    @bg.push_task()
    def do_mult(self):
        self.num *= self.mul

    def __init__(self, id, imul):
        self.mul = imul
        self.num = 1
        self.id = id

        self.bg_task = self.do_task()

    def __del__(self):
        # you should make sure that the the 
        # function is no longer in execution
        # before continuing this function
        self.bg_task.terminate()

if __name__ == '__main__':
    inst_a = Some_App(1, 2)
    task_a = inst_a.do_task()
    inst_b = Some_App(5, 6)
    task_b = inst_b.do_task()

    print('')
    inst_a.do_mult()
    inst_b.do_mult()
    time.sleep(0.6)

    print('')
    inst_a.do_mult()
    inst_b.do_mult()
    time.sleep(1.2)

    bg.terminate()
