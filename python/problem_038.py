#!/usr/bin/env python3
import time


def blurb():
    print("""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
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
        sequential_digits = set(range(1,10))
        difference_between_seq_and_set = sequential_digits.difference(digit_set)
        if len(difference_between_seq_and_set) == 0:
            return True
    return False


def find_concatenated_pandigital_products(upper_bound):
    combine_number = lambda x, y: int(str(x) + str(y))
    find_product = lambda x, y: x * y
    upper_bound += 1
    pandigital_numbers = [x for x in range(1,upper_bound) if is_pandigital(x)]
    products = set()
    result_p = result_m = result_n = 0
    for multiplicand in pandigital_numbers:
        n = 1
        product = pandigital_check = multiplicand
        while is_pandigital(pandigital_check):
            product_statement = "%d x %d = %d" % (multiplicand, n, product)
            if pandigital_check > result_p:
                result_p = pandigital_check
                result_m = multiplicand
                result_n = n
            n += 1
            product = find_product(multiplicand, n)
            pandigital_check = combine_number(pandigital_check, product)
    n_string = " x ".join([str(x) for x in range(1, result_n + 1)])
    print("%d x %s = %d" % (result_m, n_string, result_p))
    return result_p


def main():
    blurb()
    start = time.time()
    RESULT = find_concatenated_pandigital_products(10000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
