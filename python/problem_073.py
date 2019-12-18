#!/usr/bin/env python3
import time
import sys
from math import gcd
sys.setrecursionlimit(10000)


def problem_output(func, *args):
    def wrapper(*args):
        blurb()
        start = time.time()
        result = func(*args)
        time_to_end = time.time() - start
        print(f"Result: {result}")
        print(f"Completed in {time_to_end}")

    return wrapper


def blurb():
    print(
        """
    Consider the fraction, n/d, where n and d are positive integers. If n<d and
    HCF(n,d)=1, it is called a reduced proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order
    of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
    5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that there are 3 fractions between 1/3 and 1/2.

    How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
    proper fractions for d ≤ 12,000?
    """
    )


def eratosthenes_sieve(number):
    primes = [True] * number
    primes[0], primes[1] = [False] * 2
    primes_list = []
    for ind, value in enumerate(primes):
        if value is True:
            primes[ind * 2 :: ind] = [False] * (((number - 1) // ind) - 1)
            primes_list.append(ind)
    return primes_list


def farey_sequence(max_denominator, from_denominator, to_denominator):
    mediant_denominator = from_denominator + to_denominator
    if max_denominator < mediant_denominator:
        return 0
    return (
        1
        + farey_sequence(max_denominator, from_denominator, mediant_denominator)
        + farey_sequence(max_denominator, mediant_denominator, to_denominator)
    )


@problem_output
def problem(max_denominator, from_denominator, to_denominator):
    return farey_sequence(max_denominator, from_denominator, to_denominator)


def main():
    problem(12000, 3, 2)


if __name__ == "__main__":
    main()
