#!/usr/bin/env python3
import time

def blurb():
    print("""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """)

def get_factorial_sum(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result

def find_factorial_numbers():
    '''
    The upper bound of these solutions is:
    '''
    upper_bound = get_factorial_sum(9) * 7
    result = []
    list_digits = lambda x: [int(y) for y in str(x)]
    for number in range(10, upper_bound):
        sum_of_facts = 0
        for digit in list_digits(number):
            sum_of_facts += get_factorial_sum(digit)
        if sum_of_facts == number:
            result.append(number)
            print(number)
    return sum(result)

def main():
    blurb()
    start = time.time()
    RESULT = find_factorial_numbers()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
