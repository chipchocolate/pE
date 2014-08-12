#!/usr/bin/python

import math

solutions = []
perimeter = []
steps = []
exp = 210

for j in range(1, 1001, 2):
    steps.append(exp)
    exp += exp

for p in steps:
    if p > 1000:
        break
    start = int(math.sqrt(p)) - 1
    end = int(p / 2) + 1
    for a in range(start, end):
        for b in range(start + 1, end):
            for c in range(start + 2, end):
                if a + b + c == p and a < b < c and \
                        pow(a, 2) + pow(b, 2) == pow(c, 2):
                    solutions.append((a, b, c, p))
                    perimeter.append(p)
                    print a, b, c, '\t', p

count = []
peri = []

for p in perimeter:
    if p not in peri:
        c = perimeter.count(p)
        count.append(c)
        peri.append(p)
print "The perimeter is:", peri[count.index(max(count))]
