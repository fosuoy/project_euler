#!/usr/bin/python
# Amicable numbers
# https://projecteuler.net/problem=21
#
# Let d(n) be defined as the sum of proper divisors of n 
#        (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and 
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


import time

end = 10001

def get_divisors():
  list_of_proper_divisors=[]
  for divisble in range(0,end):
    divisors=[]
    for number in range(1,divisble):
      evaluate = divisble % number
      if evaluate == 0:
        divisors.append(number)
    if not divisors: divisors=[0]
    list_of_proper_divisors.append(divisors)
  return list_of_proper_divisors

def get_amicable_numbers(list_of_proper_divisors):
  amicable_numbers=[]
  for number in range(0,end):
    amicable_a = sum(list_of_proper_divisors[number])
    if amicable_a < end:
      amicable_b = sum(list_of_proper_divisors[amicable_a])
    else:
      amicable_a = 0
      amicable_b = 0
    if amicable_b == number and amicable_b != amicable_a:
      amicable_numbers.append(number)
  amicable_numbers[:] = (value for value in amicable_numbers if value != 0)
  return amicable_numbers

start = time.time()
list_of_proper_divisors = get_divisors()
result = sum(get_amicable_numbers(list_of_proper_divisors))
elapsed = time.time() - start
 
print "Result %s found in %s seconds" % (result, elapsed)
