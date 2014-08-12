#!/usr/bin/python


def fibo():
    x, y = 1, 2
    while x < 4000000:
        yield x
        x, y = y, x + y

fibnum = fibo()
data = []

for i in fibnum:
    if i % 2 == 0:
        data.append(i)

print "The sum of fibonacci numbers that are below 4 million is: ", sum(data)
