#!/usr/bin/python
# Power Digit Sum
# https://projecteuler.net/problem=16
# Sum of indivdual digits of 2^1000

import time

base = 2
exponent = 1000
 
def sum_digits_of_power(base, exponent):
    result = []
    result.append(pow(base, exponent))
    numbers = str(result[0])
    result.append(sum(int(number) for number in numbers))
    return result
 
start = time.time()
result = sum_digits_of_power(base, exponent)
elapsed = time.time() - start
 
print("Calculated: %s to power of %s:" % (base, exponent))
print(result[0])
print("\nresult %s found in %s seconds" % (result[1], elapsed))
