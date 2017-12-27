#!/usr/bin/env python3
import time

def blurb():
    print("""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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

def rotate_number(number):
    return [int(number[n:] + number[:n]) for n in range(1, len(number) + 1)]

def find_circular_primes(upper_bound):
    '''
    reusing eratosthenes_sieve from problem 27, the rest is straightforward
    '''
    reverse_number = lambda x: int(str(x)[::-1])
    primes = eratosthenes_sieve(upper_bound)
    primes_set = set(primes)
    results = set()
    for prime in primes:
        test = set(rotate_number(str(prime)))
        if len(test) == len(test.intersection(primes_set)):
            print(prime)
            results.add(prime)
    print(len(primes))
    return len(results)

def main():
    blurb()
    start = time.time()
    RESULT = find_circular_primes(1000000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
