#!/usr/bin/env python3
import time

def blurb():
  print("""

  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

  """)

def check_factors(FACTORS, number):
  for factor in FACTORS:
    if number % factor != 0:
      return False
  return True

def main():

  start = time.time()

  FACTORS = [11,12,13,14,15,16,17,18,19,20]

  NUMBER = 2520

  is_factor = False

  while not is_factor:
    is_factor = check_factors(FACTORS, NUMBER)
    NUMBER += 20

  RESULT = NUMBER - 20

  end   = time.time() - start

  print("Result: %s"      % RESULT)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
