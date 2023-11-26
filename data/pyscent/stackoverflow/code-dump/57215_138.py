class PriorityElem:
    def __init__(self, elem_to_wrap):
        self.wrapped_elem = elem_to_wrap

    def __lt__(self, other):
        return self.wrapped_elem.priority < other.wrapped_elem.priority
