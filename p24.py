#!/usr/bin/python

# a = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
a = ["0123456789"]

while True:
    first = []
    second = []
    sequence = a[len(a) - 1]
    print sequence

    for i, x in enumerate(sequence):
        if i != (len(sequence) - 1) and x < sequence[i + 1]:
            first.append(i)
    if len(first) == 0:
        break
    k = max(first)

    for j, y in enumerate(sequence):
        if sequence[k] < sequence[j]:
            second.append(j)
    l = max(second)

    sequence[k], sequence[l] = sequence[l], sequence[k]
    last = sequence[k + 1:]
    next_seq = sequence[:k + 1]
    last.reverse()
    next_seq.extend(last)
    a.append(next_seq)

# print "The one millionth order is: ", a[999998]
