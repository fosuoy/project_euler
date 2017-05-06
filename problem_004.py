#!/usr/bin/env python3
import time

def blurb():
  print("""

  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

  Find the largest palindrome made from the product of two 3-digit numbers.

  """)

def main():
  start = time.time()

  LOWER_LIMIT = 10000
  UPPER_LIMIT = 998001

  NUMBERS = list( range(UPPER_LIMIT, LOWER_LIMIT, -1) )
  PALINDROMES = []

  for number in NUMBERS:
    number = str(number)
    if number == number[::-1]:
      PALINDROMES.append( int(number) )
  
  sorted(PALINDROMES)

  THREE_DIGIT_PALINDROMES = set()

  for factor in range(999,100,-1):
    for palindrome in PALINDROMES[::-1]:
      if palindrome % factor == 0 and 10 > int((palindrome / factor) / 100) > 1 :
          THREE_DIGIT_PALINDROMES.add(palindrome)

  RESULT = max(THREE_DIGIT_PALINDROMES)

  print(RESULT)

  end   = time.time() - start
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
