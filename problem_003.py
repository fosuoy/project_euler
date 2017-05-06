#!/usr/bin/env python3
import time

def blurb():
  print("""

  The prime factors of 13195 are 5, 7, 13 and 29.

  What is the largest prime factor of the number 600851475143 ?

  """)

def main():
  UPPER_LIMIT = 600851475143

  start = time.time()

  FACTOR = 2
  while FACTOR * FACTOR < UPPER_LIMIT:
    while UPPER_LIMIT % FACTOR == 0:
      UPPER_LIMIT = UPPER_LIMIT / FACTOR
    FACTOR += 1

  RESULT = UPPER_LIMIT

  end   = time.time() - start
  print("Result: %s"      % RESULT)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
