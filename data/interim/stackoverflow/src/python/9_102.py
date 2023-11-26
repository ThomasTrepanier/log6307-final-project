from psutil import Process

def memory_test():
    a = []
    for i in range(10000):
        a.append(i)
    del a

print(process.memory_info().rss)  # Prints 29728768
memory_test()
print(process.memory_info().rss)  # Prints 30023680
