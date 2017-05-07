#!/usr/bin/env python3
import time

def blurb():
  print("""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

  """)

def find_pythagorean_triplet(number):
  for i in range(1,number):
    for j in range(1, number - i):
      k = number - i - j
      if i**2 + j**2 == k**2:
        return i * j * k
  return False

def main():

  start = time.time()

  RESULT = find_pythagorean_triplet(1000)

  end   = time.time() - start

  print("Result: %s"      % RESULT)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
