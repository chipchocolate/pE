#!/usr/bin/python

# This code finds the largest palindrome product
# generated from the product of three 3-digit numbers.


a = b = range(100, 999)
ax = []
palindrome = []


def reverse_int(integer):
    return int(str(integer)[::-1])

for i in a:
    for j in b:
        n = i * j
        ax.append(n)

for x in ax:
    if x == reverse_int(x):
        palindrome.append(x)

palindrome.sort()

print palindrome
