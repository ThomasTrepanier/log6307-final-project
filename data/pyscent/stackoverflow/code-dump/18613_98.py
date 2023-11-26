from itertools import groupby

class CountKey:
    def __init__(self, what):
        self.what = what
        self.count = 0
    def __call__(self, item):
        count = self.count
        if item == self.what:
            self.count += 1
        return count

up = [list(g) for k, g in groupby(down, CountKey('b'))]
