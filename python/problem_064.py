#!/usr/bin/env python3
import decimal
import time


def blurb():
    print("""


    All square roots are periodic when written as continued fractions and can be
    written in the form:
    √N = a0 + 1 / (a1 + 1 / (a2 + 1 / (a3 + 1 / ...)))

    It can be seen that the sequence is repeating. For conciseness, we use the
    notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
    indefinitely.

    The first ten continued fraction representations of (irrational) square roots are:

    √2=[1;(2)], period=1
    √3=[1;(1,2)], period=2
    √5=[2;(4)], period=1
    √6=[2;(2,4)], period=2
    √7=[2;(1,1,1,4)], period=4
    √8=[2;(1,4)], period=2
    √10=[3;(6)], period=1
    √11=[3;(3,6)], period=2
    √12=[3;(2,6)], period=2
    √13=[3;(1,1,1,1,6)], period=5
    Exactly four continued fractions, for N ≤ 13, have an odd period.
    How many continued fractions for N ≤ 10000 have an odd period?
    """)


def get_period(period):
    '''
    Fraction to determine period of repeating number list
    '''
    list_len = len(period)
    result = False
    for number in range(1, (list_len // 2) + 1):
        period_list = period[:number] * (list_len // number)
        if (list_len % number) == 0:
            if period_list == period:
                result = number
                break
        else:
            endpoint = list_len - (list_len % number)
            if period_list == period[:endpoint]:
                result = number
                break
    return result


def continued_fraction(something):
    '''
    Generator for getting next item in continued fraction
    '''
    context = decimal.Context(prec=500)
    sqrt_number = context.sqrt(something)
    aPrevious = int(sqrt_number)
    denominator = context.add(sqrt_number, aPrevious)
    while denominator != 0:
        yield aPrevious
        denominator = context.add(sqrt_number, -aPrevious)
        sqrt_number = context.divide(1, denominator)
        aPrevious = int(sqrt_number)


def calculate_continued_fraction_period(number):
    '''
    Get the period of the continued fraction for the square root
    '''
    period = []
    CF = continued_fraction(number)
    result = 0
    for count, integer in enumerate(CF):
        if count == 0:
            continue
        if len(period) > number ** 2:
            break
        period.append(integer)
        result = get_period(period)
        if result and len(period) > 14:
            return result
    return result


def problem_064(upper_range):
    number_of_odd_periods = 0
    for number in range(2, upper_range + 1):
        if number % 10 == 0:
            print('.', end='', flush=True)
        if number ** 0.5 % 1 != 0:
            period = calculate_continued_fraction_period(number)
            if period % 2 != 0:
                number_of_odd_periods += 1
    print('Done')
    return number_of_odd_periods


def main():
    blurb()
    start = time.time()
    RESULT = problem_064(10000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
