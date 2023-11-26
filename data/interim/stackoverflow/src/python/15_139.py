class PriorityElem:
    def __init__(self, elem_to_wrap, priority):
        self.wrapped_elem = elem_to_wrap
        self.priority = other.priority

    def __lt__(self, other):
        return self.priority <  other.priority
