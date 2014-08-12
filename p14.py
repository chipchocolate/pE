#!/usr/bin/python

# This algorithmic code finds longest collatz sequence that starts with
# a number below one million.


def collatz_seq(n):
    seq = []
    seq.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            seq.append(n)
        elif n % 2 != 0:
            n = (3 * n) + 1
            seq.append(n)
    return seq

lst = []
count = 0

for i in xrange(1, 1000000):
    a = collatz_seq(i)
    lst.append(a)
    print count
    count = count + 1

b = max(lst, key=len)
print b
print len(b)
