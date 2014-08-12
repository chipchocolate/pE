#!/usr/bin/python

import math

hun_fact = math.factorial(100)

hun_fact = str(hun_fact)

sum = 0
for i in hun_fact:
    i = int(i)
    sum += i

print sum
