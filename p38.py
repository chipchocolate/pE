#!/usr/bin/python

string = ""
f = ""
lst = []

for n in range(1, 1000000):
    for x in range(1, 6):
        count = 1
        temp = []
        for i in range(1, x + 1):
            c = n * i
            for j in str(c):
                string += j
        for k in string:
            if string.count(k) == 1:
                continue
            else:
                string = ""
        if len(string) == 9 and '0' not in string:
            print string, n
            lst.append(int(string))
        string = ""
