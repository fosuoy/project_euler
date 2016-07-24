#!/usr/bin/python
# Lattice paths
# Using https://en.wikipedia.org/wiki/Combination
# Test results against standard problem_015.py
# Uses combination equation:
# n      n!
# k = k!(n-k)!

import time
 
grid = [20,20]
 
factorial = lambda b: (lambda a, b: a(a, b))(lambda a, b: b*a(a, b-1) if b > 0 else 1,b)

def Get_Result(lattice):
    n = sum(lattice)
    k = lattice[1]
    result = factorial(n) / (factorial(k) * factorial(n-k))
    return result

start = time.time()
result = Get_Result(grid)
elapsed = time.time() - start
 
print "result %s found in %s seconds" % (result, elapsed)
