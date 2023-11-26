import random
import statistics as stats
from collections import Counter as counter
from timeit import Timer

def slice_impl(l):
  l.sort()
  res = l[::2]

def dict_impl(l):
  count={}
  res=[]
  for i in l:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1
    if count[i] % 2:
      res.append(i)

def counter_impl(l):
  count = counter(l)
  res = []
  for key, val in count.items():
    res.extend(val//2 * [key])

def set_impl(l):
  bag = set()
  res = []
  for i in l:
    if i in bag:
      res.append(i)
      bag.remove(i)
    else:
      bag.add(i)

def timed_run():
  for name, func in {"Sort and Slice": slice_impl, 
                     "Dictionary": dict_impl, 
                     "Counter": counter_impl, 
                     "Set": set_impl}.items():
    seq = list(range(50))*2
    results = []
    print(f"{name} Implementation Results")
    for i in range(50):
      if len(results) % 10: random.shuffle(seq) # shuffle after 10 runs
      results.append(Timer(lambda: func(seq)).timeit(10**4))
      # print(f"Run {i+1:02}: {results[i]:.6f}")
    print("")
    print(f"Median:  {stats.median(results):.6f}")
    print(f"Mean:    {stats.mean(results):.6f}")
    print(f"Std Dev: {stats.stdev(results):.6f}")
    print("\n\n")

timed_run()
