#!/usr/bin/python


def checker():
    n = 0
    penta = []
    hexa = []
    while True:
        n += 1
        t = n * (n + 1) * 0.5
        p = n * ((3 * n) - 1) * 0.5
        h = n * ((2 * n) - 1)
        penta.append(p)
        hexa.append(h)
        if t in penta and t in hexa and t != 1 and t != 40755:
            return t

print checker()
