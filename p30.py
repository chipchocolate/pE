#!/usr/bin/python

found = []

for n in xrange(2, 10000001):
    n = "{0:07d}".format(n)
    n = str(n)
    a, b, c, d, e, f, g = n[0], n[1], n[2], n[3], n[4], n[5], n[6]
    sol = pow(int(a), 6) + pow(int(b), 6) + pow(int(c), 6) + \
        pow(int(d), 6) + pow(int(e), 6) + pow(int(f), 6) + \
        pow(int(g), 6)
    n = "{0:01d}".format(int(n))
    if int(n) == sol:
        found.append(int(n))
        print n

print found, "The sum is:", sum(found)
