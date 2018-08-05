#!/usr/bin/env python3
import time

def blurb():
  print("""


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

  """)

def main():
  start = time.time()
  LIMIT = 1000
  MULTIPLES = set()
  for number in range(0,LIMIT):
    if number % 3 == 0 or number % 5 == 0:
      MULTIPLES.add(number)
  end   = time.time() - start
  print("Result is %s" % sum(MULTIPLES))
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
