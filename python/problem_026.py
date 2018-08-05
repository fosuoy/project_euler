#!/usr/bin/env python3
from math import pow
import time

def blurb():
  print("""

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10  =   0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

  """)

def find_reoccurring(number):
  fraction  = str( int( 1 / number * pow(10, 17) ) )
  sequences = set( fraction.split( fraction[0] ) )
  return max( sequences )

def main():
  blurb()
  start = time.time()

  max_reoccuring = 0

  for i in range(1, 10):
    sequence = int( find_reoccurring( i ) )
    if sequence > max_reoccuring:
      max_reoccuring = sequence
      print(max_reoccuring)
      result = i

  end   = time.time() - start
  print("Result: %s" % result)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
