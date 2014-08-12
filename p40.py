#!/usr/bin/python

d = "." + "".join(map(str, range(1, 190000)))

cal = int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10 ** 4]) * \
    int(d[10 ** 5]) * int(d[10 ** 6])

print cal
