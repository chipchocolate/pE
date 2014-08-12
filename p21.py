#!/usr/bin/python

import factor

factors = []

for i in range(1, 10001):
    a = factor.factors(i)
    a = list(a)
    list.sort(a)
    a.pop()
    factors.append(a)

lst = []
for number, fact in enumerate(factors, 1):
    add = sum(fact)
    for j, a in enumerate(factors, 1):
        if add == j and number != j and sum(a) == number:
            print number, j
            if number not in lst:
                lst.append(number)
            if j not in lst:
                lst.append(j)

print lst
print sum(lst)
