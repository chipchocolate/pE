#!/usr/bin/python

# Sub-string divisiblity

# import re

fi = open("0-9pandigital_num.txt", "r")
found = []

for n in fi:
    a, b, c, d, e, f, g = n[1:4], n[2:5], n[3:6], n[4:7], n[5:8], \
        n[6:9], n[7:]
    if int(a) % 2 == 0 and int(b) % 3 == 0 and int(c) % 5 == 0 \
            and int(d) % 7 == 0 and int(e) % 11 == 0 \
            and int(f) % 13 == 0 and int(g) % 17 == 0:
        print n
        found.append(int(n))

print "The Sum is:", sum(found)
fi.close()
