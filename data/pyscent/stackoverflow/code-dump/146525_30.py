#!/bin/python3

import math
import os
import random
import re
import sys    
import calendar
import datetime
from collections import Counter

def usingcalendar(datetuple):
    # Write your code here
    year = datetuple[0]
    temp = list(datetuple)
    if (year%4==0):
        temp[1] = 2
        datetuple = tuple(temp)
    print(calendar.month(datetuple[0],datetuple[1]))

    obj = calendar.Calendar()
    l = []
    dt=list(datetuple)
    obj = calendar.Calendar()
    for day in obj.itermonthdates(dt[0], dt[1]):
        l.append(day)
    rev = l[:-8:-1]
    rev.reverse()
    print(rev)

    try:
        print(datetime.date(datetuple[0],datetuple[1],29).strftime('%A'))
    except ValueError:
        print("Monday")

if __name__ == '__main__':
    qw1 = []

    for _ in range(3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
        
    tup=tuple(qw1)

    usingcalendar(tup)
