#!/usr/bin/python

# This code finds the smallest number that is evenly
# divisible by each number from 1 to 20

isdivisible = []
for i in xrange(200000000, 1000000001):
    if all(i % n == 0 for n in range(1, 21)):
        isdivisible.append(i)
        print i

isdivisible.sort()
print isdivisible
