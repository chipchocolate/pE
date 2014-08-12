#!/usr/bin/python

numbers = []
steps = 2
count = 0
n = 1

while n < 1002002:
    print n
    numbers.append(n)
    n += steps
    count += 1
    if count == 4:
        count = 0
        steps += 2

print "The sum is: ", sum(numbers)
