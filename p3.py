#!/usr/bin/python

import prime

b = []

a = int(raw_input("Enter the last prime number " +
                  "that you want to generate: "))

prime_numbers = prime.gen_primes(a)

for i in prime_numbers:
    print i
    b.append(i)

c = int(raw_input("Enter the no. that you want to find " +
                  "the largest factor of: "))

for j in reversed(b):
    if c % j == 0:
        print "The largest prime factor of ", \
            c, " is: ", j
        break
