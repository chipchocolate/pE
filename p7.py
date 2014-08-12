#!/usr/bin/python

import prime

primes = []
a = prime.genprimes(1000000)

for i in a:
    primes.append(i)

print "The 10,001th prime number is: ", primes[10000]
