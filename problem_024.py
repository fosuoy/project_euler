#!/usr/bin/env python3
import time

def blurb():
  print("""


  A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                  012   021   102   120   201   210

  What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
  """)

def find_permutations(list_of_digits):
  n = len(list_of_digits)

  i = n - 2
  while i >= 0 and list_of_digits[i] >= list_of_digits[i + 1]:
    i -= 1
  if i == -1:
    return False
  j = i + 1
  while j < n and list_of_digits[j] > list_of_digits[i]:
    j += 1
  j -= 1
  list_of_digits[i], list_of_digits[j] = list_of_digits[j], list_of_digits[i]
  left  = i + 1
  right = n - 1
  while left < right:
    list_of_digits[left], list_of_digits[right] = \
                                     list_of_digits[right], list_of_digits[left]
    left  += 1
    right -= 1
  return list_of_digits

def main():
  start = time.time()
  blurb()

  number_of_permuatations = 1000000

  list_of_digits          = [0,\
                             1,\
                             2,\
                             3,\
                             4,\
                             5,\
                             6,\
                             7,\
                             8,\
                             9]

  count = 1
  while count < number_of_permuatations:
    result = find_permutations( list_of_digits )
    if not result:
      break
    count += 1

  result = ''.join( str(x) for x in result )

  end   = time.time() - start
  print("Result is: %s" % result)
  print("Completed in: %s" % end)

if __name__ == '__main__':
  main()
