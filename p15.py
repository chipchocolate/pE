#!/usr/bin/python

# This algorithmic code computes all the possible routes for a
# lattice grid

import math


def lattice_paths(a, b):
    return math.factorial(a + b) / (math.factorial((a + b) - b)
                                    * math.factorial(b))


m = n = input("Please enter a grid number: ")
ways = lattice_paths(m, n)
print "There are ", ways, "routes to get to the bottom right corner of a",\
    m, "x", n, " grid."

print len(ways)
