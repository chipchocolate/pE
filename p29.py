#!/usr/bin/python

data = []

for a in range(2, 101):
    for b in range(2, 101):
        power = pow(a, b)
        if power not in data:
            data.append(power)

print len(data)
