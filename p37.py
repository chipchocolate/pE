#!/usr/bin/python

import prime

p = prime.genprimes(10000000)

primes = []
trun_primes = []

print "[i] Generating primes..."

string = "2357"

for i in p:
    primes.append(i)
    print i

print "[+] Primes generated."

count = 0

for pr in primes:
    q = str(pr)
    print int(q), '\t', count, '\t', trun_primes
    # print int(q[:len(q) - 1]), int(q[:len(q) - 2]), int(q[:len(q) - 3]),
    #     int(q[:len(q) - 4]), int(q[:len(q) - 5]), int(q[:len(q) - 6]), \
    #     int(q[:len(q) - 7])
    if q[0] in string and q[len(q) - 1] in string:
        q = q.zfill(len(q))
        if int(q):
            if all(int(q[:len(q) - k]) in primes for k in range(1, len(q) - 1)) and \
                    all(int(q[l:]) in primes for l in range(1, len(q) - 1)) and \
                    len(q) > 1:
                count += 1
                print '\t', int(q)
                trun_primes.append(int(q))
                if count > 10:
                    print trun_primes
                    print "Sum is:", sum(trun_primes)
                    break
