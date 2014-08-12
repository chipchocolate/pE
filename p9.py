#!/usr/bin/python

# This code finds the product of the Pythagorean triplets from the sum of
# the triplets.

a = b = c = range(1, 501)

for i in a:
    for j in b:
        for k in c:
            if (i ** 2) + (j ** 2) == k ** 2 and i < j < k \
                    and i + j + k == 1000:
                p = i * j * k
                print "The triplets are: ", i, ",", j, ",", k, " and" \
                    "their product is: ", p
                break
