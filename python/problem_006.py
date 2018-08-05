#!/usr/bin/env python3
import time

def blurb():
  print("""

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

  """)

def difference_in_squares(LIMIT):
  SQUARES   = set()
  RANGE     = set( range( 1, LIMIT + 1 ) )
  RANGE_SUM = sum( RANGE )
  for i in RANGE:
    SQUARES.add( i * i )
  return ( RANGE_SUM * RANGE_SUM ) - sum( SQUARES )
    

def main():

  start = time.time()

  RESULT = difference_in_squares(100)

  end   = time.time() - start

  print("Result: %s"      % RESULT)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
