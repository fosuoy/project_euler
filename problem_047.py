#!/usr/bin/env python3
import time

def blurb():
    print("""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
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


def find_prime_factors(number, primes_list, primes_set):
    result = set()
    remain = number
    for prime in primes_list:
        if prime * prime > number: break
        found = False
        while remain % prime == 0:
            result.add(prime)
            remain = remain / prime
            found = True
        if found:
            if remain in primes_set:
                result.add(int(remain))
    return result


def find_consecutive_distinct_primes(distinct_primes):
    primes = eratosthenes_sieve(1000)
    primes_set = set(primes)
    r_difference = distinct_primes - 1
    last_lines = [""] * distinct_primes
    numbers_with_prime_multiplicands = set()
    for number in range(1,1000000):
        prime_factors = find_prime_factors(number, primes, primes_set)
        if len(prime_factors) >= distinct_primes:
            numbers_with_prime_multiplicands.add(number)
            prime_factors = [str(x) for x in prime_factors]
            last_lines.append((" x ".join(prime_factors) + " = " + str(number)))
            last_lines.pop(0)
            mx_mupds = max(numbers_with_prime_multiplicands)
            r_numbers = set(range(mx_mupds - r_difference, mx_mupds))
            r_intersection = len(r_numbers.intersection(numbers_with_prime_multiplicands))
            if r_intersection >= r_difference:
                for line in last_lines: print(line)
                return number - r_difference


def main():
    blurb()
    start = time.time()
    RESULT = find_consecutive_distinct_primes(4)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
