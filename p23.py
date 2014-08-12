#!/usr/bin/python

import factor

abundant = []
temp_final = []
final = []

for i in range(1, 28124):
    fact = factor.factors(i)
    fact = list(fact)
    fact.sort()
    fact.pop()
    if sum(fact) > i:
        abundant.append(i)

for num in abundant:
    for nums in abundant:
        addition = num + nums
        if addition < 28124:
            if addition not in temp_final:
                print num, addition
                temp_final.append(addition)

print temp_final

for number in range(1, 28124):
    if number not in temp_final:
        final.append(number)

print final
print sum(final)
