from simple_benchmark import BenchmarkBuilder
from heapq import nsmallest


b = BenchmarkBuilder()

@b.add_function()
def MehrdadPedramfar(A):
    return [sorted(i)[1] for i in zip(*A)]

@b.add_function()
def NicolasGervais(A):
    return np.sort(A, axis=0)[1, :]

@b.add_function()
def imcrazeegamerr(A):
    rotated = zip(*A[::-1])

    result = []
    for arr in rotated:
        # sort each 1d array from min to max
        arr = sorted(list(arr))
        # add the second minimum value to result array
        result.append(arr[1])

    return result

@b.add_function()
def Daweo(A):
    return np.apply_along_axis(lambda x:heapq.nsmallest(2,x)[-1], 0, A)

@b.add_function()       
def kederrac(A):
    return [nsmallest(2, e)[-1] for e in zip(*A)]


@b.add_arguments('Number of row/cols (A is  square matrix)')
def argument_provider():
    for exp in range(2, 18):
        size = 2**exp
        yield size, [[randint(0, 1000) for _ in range(size)] for _ in range(size)]

r = b.run()
r.plot()
