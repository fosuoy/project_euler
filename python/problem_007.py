#!/usr/bin/env python3
import time

def blurb():
  print("""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

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

def get_prime(number):
  count = 1
  prime = 0
  CHECK = 3
  while count < number:
    if is_prime(CHECK):
      prime = CHECK
      count += 1
    CHECK += 2
  CHECK -= 2
  return CHECK

def main():

  start = time.time()

  RESULT = get_prime(10001)

  end   = time.time() - start

  print("Result: %s"      % RESULT)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
