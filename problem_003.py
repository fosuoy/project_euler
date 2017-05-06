#!/usr/bin/env python3
import time

def blurb():
  print("""

  The prime factors of 13195 are 5, 7, 13 and 29.

  What is the largest prime factor of the number 600851475143 ?

  """)

def main():
  LIMIT = 600851475143

  start = time.time()

  i = 2
  while i * i < LIMIT:
    while LIMIT % i == 0:
      LIMIT = LIMIT / i
    i += 1

  RESULT = LIMIT

  end   = time.time() - start
  print("Result: %s"      % RESULT)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
