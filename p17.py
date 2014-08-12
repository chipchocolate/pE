#!/usr/bin/python

# This module is an algorithm that writes all the numbers
# below the given number in words and sums all the numbers
# excluding the characters ",", "-" and space " ".

import num2words
n = input("Enter n, for range(1, n): ")
words = []

for i in range(1, n):
    a = str(num2words.num2words(i)).title()
    words.append(a)

print words

count = 0
for j in words:
    for k in j:
        if k != " " and k != "-" and k != ",":
            count += 1

print count
