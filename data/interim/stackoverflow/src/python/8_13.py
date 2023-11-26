import timeit

def pattern1():
  title = ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
  counts = {}
  for word in title:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1

def pattern2():
  title = ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
  counts = {}
  for word in title:
    if word not in counts:
      counts[word] = 1
    else:
      counts[word] += 1

sample1 = [timeit.timeit(pattern1, number=10000) for _ in range(10)]
sample2 = [timeit.timeit(pattern2, number=10000) for _ in range(10)]

print(sum(sample1) / len(sample1))
# 0.01713230140048836
print(sum(sample2) / len(sample2))
# 0.017954919600015273
