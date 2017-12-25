#!/usr/bin/env python3
import time

def blurb():
    print("""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """)

def eratosthenes_sieve(number):
    primes = [True] * number
    primes[0], primes[1] = [False] * 2
    primes_list = set()
    for ind, value in enumerate(primes):
        if value is True:
            primes[ind*2::ind] = [False] * (((number - 1)//ind)-1)
            primes_list.add(ind)
    return primes_list

def test_truncatability_r(number, primes):
    while number in primes:
        digit = number % 10
        number = (number - digit) // 10
        if number < 10 and number in primes:
            return True
    return False

def test_truncatability_l(number, primes):
    truncate = lambda x: int(str(x)[1::])
    while number in primes:
        number = truncate(number)
        if number < 10 and number in primes:
            return True
    return False

def find_truncatable_primes(upper_bound):
    primes = eratosthenes_sieve(upper_bound)
    results = []
    for prime in primes:
        if test_truncatability_r(prime, primes):
            if test_truncatability_l(prime, primes):
                print(prime)
                results.append(prime)
    return sum(results)

def main():
    blurb()
    start = time.time()
    RESULT = find_truncatable_primes(1000000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
