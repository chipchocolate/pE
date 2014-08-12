#!/usr/bin/python

a = b = range(1, 1001)
ax = []
palindrome = []


def reverse_int(integer):
    return int(str(integer)[::-1])

for x in range(0, 1000001):
    if x == reverse_int(x):
        if x not in palindrome:
            palindrome.append(x)

palindrome.sort()
sum = 0
for i in palindrome:
    b = bin(i)[2:]
    rb = reverse_int(b)
    if b == str(rb):
        sum += i
        print i, b, rb

print sum
