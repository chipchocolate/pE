#!/usr/bin/python

import prime

L = 1000
data = prime.genprimes(L)
primes = []

for i in data:
    primes.append(i)

for p in primes[::-1]:
    c = 1
    while pow(10, c, p) - 1 != 0:
        c += 1
    if p - c == 1:
        break

print "The answer is: ", p
