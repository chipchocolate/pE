#!/usr/bin/python


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(pow(n, 0.5))
    f = 5
    while f <= r:
        print '\t', f
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

num = []
a_num = []
b_num = []
n = 0

for a in xrange(-1000, 1001):
    for b in xrange(-1000, 1001):
        while True:
            p = (n ** 2) + (a * n) + b
            if is_prime(p):
                num.append(n)
                a_num.append(a)
                b_num.append(b)
                print n, a, b
                n += 1
            else:
                n = 0
                break

zipped = zip(num, a_num, b_num)
found = zipped[num.index(max(num))]
print "The max no. of primes produced:", (max(num) + 1)
print num.index(max(num))
print "(n, a, b) is: ", zipped[num.index(max(num))]
print "Multipication of a and b that produced the max no. of primes is: ",\
    (found[1] * found[2])
