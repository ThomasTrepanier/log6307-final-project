l = list(range(1,6))
def index_generator():
    while True:
        yield 0
        yield -1

index = index_generator()
result = []
while l:
    result.append(l.pop(next(index)))
