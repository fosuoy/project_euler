#!/usr/bin/env python3
import time
import math

def blurb():
  print("""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
  """)

def power_sum(power):
    powers = {}
    result = []
    for number in range(0,10):
        powers[number] = math.pow(number, power)
    upper_range = int(math.pow(9, power) * power)
    for number in range(10,upper_range):
        test = 0
        for item in map(int, str(number)):
            test += powers[item]
        if number == test:
            result.append(number)
    return sum(result)

def main():
    blurb()
    start = time.time()
    RESULT = power_sum(5)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
