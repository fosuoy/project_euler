#!/usr/bin/env python3
import time

def blurb():
  print("""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

  """)

def is_prime(n):
  if n <= 1:
    return False
  elif n <= 3:
    return True
  elif n % 2 == 0 or n % 3 == 0:
    return False

  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i = i + 6
  return True

def find_primes(LIMIT):
  NUMBERS = set( range( 1,LIMIT ) )
  PRIMES  = set()
  for number in NUMBERS:
    if is_prime(number):
      PRIMES.add(number)
  return PRIMES

def main():

  start = time.time()

  LIMIT  = 2000000

  RESULT = sum( find_primes(LIMIT) )

  end    = time.time() - start

  print("Result: %s"      % RESULT)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
