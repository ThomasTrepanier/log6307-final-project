def count(func):
    def counted(value):
        counted.call_count += 1
        return func(value)
    counted.call_count = 0
    return counted
