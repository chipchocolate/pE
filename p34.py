#!/usr/bin/python

import math

found = []

for n in xrange(10, 50000):
    split_n = list(str(n))
    f = 0
    for i in split_n:
        i = int(i)
        f += math.factorial(i)
    if f == n:
        found.append(n)

print "Sum is: ", sum(found)
