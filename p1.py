#!/usr/bin/python

data = [i for i in range(1000)]
sort = []

for i in data:
    if i % 3 == 0 or i % 5 == 0:
        sort.append(i)

print sum(sort)
