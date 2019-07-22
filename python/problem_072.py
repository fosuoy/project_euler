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

    It can be seen that there are 21 elements in this set.

    How many elements would be contained in the set of reduced proper fractions
    for d ≤ 1,000,000?
    """)


def eratosthenes_sieve(number):
    primes = [True] * number
    primes[0], primes[1] = [False] * 2
    primes_list = []
    for ind, value in enumerate(primes):
        if value is True:
            primes[ind*2::ind] = [False] * (((number - 1)//ind)-1)
            primes_list.append(ind)
    return primes_list


def problem_072(upper_bound):
    '''
    The given example sums the euler totient of range(1, 9) so:
    Code the rules here:
    https://www.doc.ic.ac.uk/~mrh/330tutor/ch05s02.html
    i.e.
    When prime number, totient is n - 1
    When two number are coprime phi(n * m) = phi(n) * phi(m)

    Optimize then run for 1..upper_bound
    '''
    euler_totients = [x for x in range(upper_bound)]
    primes = eratosthenes_sieve(upper_bound)
    for prime in primes:
        for i in range(prime, upper_bound, prime):
            euler_totients[i] = euler_totients[i] / prime * (prime - 1)
    sum_up_to_d = sum(euler_totients)
    return int(sum_up_to_d)


def main():
    blurb()
    start = time.time()
    RESULT = problem_072(1000000)
    end = time.time() - start
    print("Result: %s" % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
