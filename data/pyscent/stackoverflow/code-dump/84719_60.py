def sample_func(queue_ref):
    for i in range(10):
        queue_ref.put(i)


IQ = IterQueue()

p = mp.Process(target=sample_func, args=(IQ,))
p.start()
p.join()

print(list(IQ))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

