#!/usr/bin/env python3
import time


def blurb():
    print("""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    """)


def check_numbers_for_same_digits():
    '''
    numbers divisble by 32...
    '''
    digits = lambda x:sorted(str(x))
    number = 1
    while not digits(number * 2) == \
              digits(number * 3) == \
              digits(number * 4) == \
              digits(number * 5) == \
              digits(number * 6):
                  number += 1 
    print("Multiples:")
    for i in range(1,7):
        print("%d * %d = %d" % (number, i, number * i))
    return number


def main():
    blurb()
    start = time.time()
    RESULT = check_numbers_for_same_digits()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
