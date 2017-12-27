#!/usr/bin/env python3
import time
import itertools

def blurb():
    print("""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
    """)

def find_pandigital_divisibility(numbers):
    divisors = [1,2,3,5,7,11,13,17]
    pandigital_numbers = \
            ["".join(x) for x in set(itertools.permutations(numbers)) if x[0] != "0"]
    results = []
    for number in pandigital_numbers:
        n = 0
        for divisor in divisors:
            number_check = int(number[n] + number[n+1] + number[n+2])
            if number_check % divisor == 0:
                if divisor == 17:
                    results.append(int(number))
                    break
                n += 1
            else:
                break
    return sum(results)

    return len(pandigital_numbers)

def main():
    blurb()
    start = time.time()
    RESULT = find_pandigital_divisibility('9876543210')
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
