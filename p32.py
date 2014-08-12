#!/usr/bin/python

found = []

for a in xrange(1, 50):
    for b in xrange(1, 1964):
        c = a * b
        if len(str(a)) + len(str(b)) + len(str(c)) == 9:
            combined = str(a) + str(b) + str(c)
            if all(str(num) in combined for num in range(1, 10)):
                if int(c) not in found:
                    found.append(int(c))
                    print c, a, b

print found
print "Sum is:", sum(found)
