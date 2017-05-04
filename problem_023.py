#!/usr/bin/env python3
import time

def blurb():
  print("""
  A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

  A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

  As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

  Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
  """)

def is_abundant_number(number):
  divisors = set()
  for divisor in range(1, int(number / 2) + 1):
    if number % divisor == 0:
      divisors.add(divisor)
  if sum(divisors) > number:
    return number
  else:
    return False

def main():
  start = time.time()

  blurb()

  ABUNDANT_NUMBERS = []
  INTEGERS_NOT_SUM_ABUNDANT_NUMBERS = []

  for number in range(1,28123):
    if is_abundant_number(number):
      ABUNDANT_NUMBERS.append(number)
  ALL_NUMBERS       = set(range(1,28123))
  SUMS_OF_ABUNDANTS = set()
  for numbera in ABUNDANT_NUMBERS:
    for numberb in ABUNDANT_NUMBERS:
      SUMS_OF_ABUNDANTS.add(numberb + numbera)
  RESULT = ALL_NUMBERS - SUMS_OF_ABUNDANTS
  print(RESULT)
  print(sum(RESULT))
      

  end   = time.time() - start
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
