from functools import total_ordering

@total_ordering
class PrioritizedItem:
    # ...

    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority
