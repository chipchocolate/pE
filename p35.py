#!/usr/bin/python

import prime

a = prime.genprimes(1000000)
pri = []
circular_primes = []
final_primes = []

for p in a:
    pri.append(str(p))

for pr in pri:
    pr = str(pr)
    if pr not in circular_primes:
        count = 0
        temp_primes = []
        temp_primes.append(pr)
        for i in range(len(pr) - 1):
            pr = pr[len(pr) - (len(pr) - 1):] + pr[0]
            temp_primes.append(pr)
            if pr in pri:
                count += 1
        pr = pr[len(pr) - (len(pr) - 1):] + pr[0]
        if count + 1 == len(str(pr)):
            circular_primes.extend(temp_primes)
            print pr
            print temp_primes

for i in circular_primes:
    if i not in final_primes:
        final_primes.append(i)

print final_primes
print len(final_primes)
