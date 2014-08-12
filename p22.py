#!/usr/bin/python

import re

data = open("names_p22.txt", 'r')

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in data:
    names = re.findall(r'"([A-Z]+)"', i)

names.sort()
score = []
print names.index("COLIN")
s = 0

for name in names:
    print name
    for ind, letter in enumerate(name):
        s += (alpha.index(letter) + 1)
        print s, letter
        if ind == len(name) - 1:
            s = s * (names.index(name) + 1)
            print s
            score.append(s)
            s = 0
print sum(score)
data.close()
