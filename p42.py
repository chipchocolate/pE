#!/usr/bin/python

# Coded triangle numbers

import re

l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

data = open("words_p42.txt", "r")
tri_num = []
tri_num = []

for n in range(1, 51):
    t = 0.5 * n * (n + 1)
    tri_num.append(t)
    print t

for d in data:
    words = re.findall(r'"([A-Z]+)"', d)

count = 0
for word in words:
    value = 0
    for letter in word:
        value += l.index(letter) + 1
    if value in tri_num:
        count += 1

print "No. of Triangle Words:", count
