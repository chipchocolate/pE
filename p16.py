#!/usr/bin/python

# This algorithmic code computes the sum of the digits of the result of
# 2 to the power of 1000


def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r

a = 2 ** 1000

print "The sum of the digits of the result of 2 to the "\
    "power of 1000 is: ", sum_digits(a)
