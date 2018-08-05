#!/usr/bin/env python3
import time

from math import sqrt


def blurb():
    print("""
            The primes 3, 7, 109, and 673, are quite remarkable. By taking any
            two primes and concatenating them in any order the result will
            always be prime. For example, taking 7 and 109, both 7109 and 1097
            are prime. The sum of these four primes, 792, represents the lowest
            sum for a set of four primes with this property.

            Find the lowest sum for a set of five primes for which any two
            primes concatenate to produce another prime.
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


def is_prime(n):
    '''
    Method to tell if a number is prime or not, returns True / False
    '''
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def combine_primes(current_numbers, possible_number):
    '''
    Creates a set of combinations between current_numbers and the
    possible_number.
    If the set is not a subset of the prime set return false
    '''
    comb = lambda x,y: int(str(x) + str(y))
    for number in current_numbers:
        if not is_prime(comb(number, possible_number)):
            return False
        if not is_prime(comb(possible_number, number)):
            return False
    return True


def loop_over_primes(compare, other_primes, breakpoint):
    '''
    Create a copy of the list of primes to test against, then take away the
    smallest member if a list of size 'breakpoint' isn't found
    '''
    other_primes_loop = other_primes.copy()
    while len(other_primes_loop) > 0:
        list_of_primes = [compare]
        for prime in other_primes_loop:
            if combine_primes(list_of_primes, prime):
                list_of_primes.append(prime)
            if len(list_of_primes) >= breakpoint:
                return list_of_primes
        other_primes_loop.pop(0)
    return []


def iterate_over_primes(primes, breakpoint):
    '''
    Iterate over each prime given attempting to find a list of 'breakpoint'
    length
    '''
    list_of_primes = []
    while len(list_of_primes) < breakpoint and len(primes) > 0:
        start = primes.pop(0)
        print("Checking: %s" % str(start))
        list_of_primes = loop_over_primes(start, primes, breakpoint)
    print("Found this list: %s" % str(list_of_primes))
    return sum(list_of_primes)


def problem_060():
    '''
    Create a range of primes to iterate over, then iterate over them!
    '''
    primes = eratosthenes_sieve(10000)
    primes = [x for x in primes if x > 3]
    return iterate_over_primes(primes, 5)


def main():
    blurb()
    start = time.time()
    RESULT = problem_060()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
