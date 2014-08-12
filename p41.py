#!/usr/bin/python

import prime

print "[i] Generating primes..."
p = prime.genprimes(10000000)

primes = []

for i in p:
    primes.append(i)

print "[+] Primes generated."

pand_primes = []

for i in reversed(primes):
    temp = ""
    for j in str(i):
        if j not in temp and j != 0 and j in str(range(1, len(str(i)) + 1)):
            temp += j
    if len(temp) == len(str(i)):
        pand_primes.append(i)
        print "Largest Palindrome prime is:", i
        break
