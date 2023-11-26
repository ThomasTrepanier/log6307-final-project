# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:10:07 2019

@author: Paddy3118
"""

from random import shuffle, random, randint

#%%
items = [5, 6, 2, 10, 2, 3, 4]

def eq(a, b):
    "Equal enough"
    return int(abs(a - b)) == 0

def fair_partition(items, jiggles=100):
    target = sum(items) / 2
    print(f"  Target sum: {target}")
    srt = sorted(items)
    a = srt[::2]    # every even
    b = srt[1::2]   # every odd
    asum = sum(a)
    bsum = sum(b)
    n = 0
    while n < jiggles and not eq(asum, target):
        n += 1
        if random() <0.5:
            # move from a to b?
            if random() <0.5:
                a, b, asum, bsum = b, a, bsum, asum     # Switch
            shuffle(a)
            trial = a[0]
            if abs(target - (bsum + trial)) < abs(target - bsum):  # closer
                b.append(a.pop(0))
                asum -= trial
                bsum += trial
                print(f"  Jiggle {n:2}: Delta after Move: {abs(target - asum)}")
        else:
            # swap between a and b?
            apos = randint(0, len(a) - 1)
            bpos = randint(0, len(b) - 1)
            trya, tryb = a[apos], b[bpos]
            if abs(target - (bsum + trya - tryb)) < abs(target - bsum):  # closer
                b.append(trya)  # adds to end
                b.pop(bpos)     # remove what is swapped
                a.append(tryb)
                a.pop(apos)
                asum += tryb - trya
                bsum += trya - tryb
                print(f"  Jiggle {n:2}: Delta after Swap: {abs(target - asum)}")
    return sorted(a), sorted(b)

if __name__ == '__main__':
    for _ in range(5):           
        print('\nFinal:', fair_partition(items), '\n')  
