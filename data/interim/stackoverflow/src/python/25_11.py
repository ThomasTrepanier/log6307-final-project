import timeit

testcode_numpy = ''' 
import numpy
def multiples_numpy(value, length):
    return numpy.arange(1, length+1) * value
multiples_numpy(5, 1000)
'''

testcode = ''' 
def multiples(value, length):
    return [*range(value, length*value+1, value)]
multiples(5, 1000)
'''

print(timeit.timeit(testcode_numpy))
print(timeit.timeit(testcode))

# Result:
# without numpy: 9.7 s
# with numpy: 2.4 s
