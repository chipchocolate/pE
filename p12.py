#!/usr/bin/python

# This algorithmic code finds the value of the first triangle number
# that has over five hundred divisors(factors)

import factor

count = 2

while True:
    tri_num = reduce(lambda x, y: x + y, xrange(1, count))
    factors = factor.factors(tri_num)
    print "No. of factors of the current triangle number is: ", len(factors)
    if len(factors) > 500:
        print "Found the first triangle number that has 500 factors," \
            " and the number is", tri_num
        break
    else:
        count += 1
