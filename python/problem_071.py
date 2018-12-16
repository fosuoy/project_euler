#!/usr/bin/env python3
import math
import time

from fractions import Fraction


def blurb():
    print("""
    Consider the fraction, n/d, where n and d are positive integers. If n<d and
    HCF(n,d)=1, it is called a reduced proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order
    of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
    5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that 2/5 is the fraction immediately to the left of 3/7.

    By listing the set of reduced proper fractions for d ≤ 1,000,000 in
    ascending order of size, find the numerator of the fraction immediately to
    the left of 3/7.
    """)


def problem_071(upper_bound):
    '''
    Initially tried bruteforcing this problem, read this solution here:
    https://www.mathblog.dk/project-euler-71-proper-fractions-ascending-order/
    
    The idea is that since:
    (p/q) < (a/b) == p * b < a * q
    Then:
    pb <= aq -1
    Then:
    p <= (aq - 1) / b

    r / s is to find the greatest p / q pair that is closest to a / b
    '''
    r_p_f_list = []
    a = 3
    b = 7
    r = 0
    s = 1
    for denominator in range(2, upper_bound + 1, 2):
        numerator = int((a * denominator - 1) / b)
        if (r * denominator) < (s * numerator):
            r = numerator
            s = denominator
    print("%d / %d" % (r, s))
    return r


def main():
    blurb()
    start = time.time()
    RESULT = problem_071(1000000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
