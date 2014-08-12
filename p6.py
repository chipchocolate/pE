#!/usr/bin/python

# This code finds the difference between the sum of squares of the first
# hundred natural numbers and the square of sum.

squares = []
num = range(1, 101)

for i in range(1, 101):
    n = i ** 2
    squares.append(n)

sum_of_sqrs = sum(squares)
sqr_of_sum = sum(num) ** 2

diff = sqr_of_sum - sum_of_sqrs
print diff
