#!/usr/bin/env python3
import time

def blurb():
    print("""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
    """)

def is_pandigital(number, check_sequential=False):
    '''
    A function to check if a number is pandigital
    '''
    digits = []
    while number % 10 != 0 or number > 1:
        digits.append(number % 10)
        number = int(number / 10)
    digit_set = set(digits)
    if len(digits) == len(digit_set) and 0 not in digits:
        if not check_sequential: return True
#        mis-understood the problem here - MUST include digits 1-9, not just be
#        sequential...
#        sequential_digits = set(range(1,max(digit_set) + 1))
        sequential_digits = set(range(1,10))
        difference_between_seq_and_set = sequential_digits.difference(digit_set)
        if len(difference_between_seq_and_set) == 0:
            return True
    return False

def pandigits(upper):
    '''
    A function to get only digits which are pandigital between 0 and upper...
    '''
    upper += 1
    number_range = range(1,upper)
    pandigital_list = []
    for number in number_range:
        if is_pandigital(number):
            pandigital_list.append(number)
    return pandigital_list

def pandigital_finder():
    '''
    Max number of digitals are:
    4 digital * 4 digits = 5 digits
    So max product will be 9876
    '''
    products = pandigits(9876)
    result = []
    multiplicands = set()
    for multiplicand_1 in products[::]:
        for product in products[::-1]:
            if product > multiplicand_1:
                if product % multiplicand_1 == 0:
                    multiplicand = product // multiplicand_1
                    if multiplicand in products:
                        all_digits = \
                                "%d%d%d" % (multiplicand_1, multiplicand, product)
                        all_digits = int(all_digits)
                        if is_pandigital(all_digits, check_sequential=True) and product not in result:
                            print("%d * %d = %d" % (multiplicand_1, multiplicand, product))
                            result.append(product)
    return sum(result)

def main():
    blurb()
    start = time.time()
    RESULT = pandigital_finder()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
