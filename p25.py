#!/usr/bin/python


def fibo():
    x, y = 1, 1
    x = str(x)
    count = 1
    while len(x) < 1001:
        print x
        if len(x) == 1000:
            print "The first term that has 1000 digits is: ", count
            break
        x = int(x)
        x, y = y, x + y
        x = str(x)
        count += 1

fibnum = fibo()
