#!/usr/bin/python
# Factorial digit sum
# https://projecteuler.net/problem=20
# Create a function to calculate factorials (n!)
# Taken from solution to problem 15

import time
 
factorial = lambda b: (lambda a, b: a(a, b))(lambda a, b: b*a(a, b-1) if b > 0 else 1,b)

start = time.time()
result = factorial(100)
elapsed = time.time() - start
 
print "Result %s found in %s seconds" % (result, elapsed)
