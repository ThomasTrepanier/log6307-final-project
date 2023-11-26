class IntegerStack:
    def __init__(self):
        self._stack = []
        self._head = -1

    def emptyStack(self):
        return self._head < 0

    def head(self):
        if self._head < 0:
            raise Exception("The stack is empty.")
        return self._stack[self._head]
