#!/usr/bin/env python3
import time
import math

def blurb():
    print("""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
    """)

def eratosthenes_sieve(number):
    primes = [True] * number
    primes[0], primes[1] = [False] * 2
    primes_list = []
    composite_numbers = []
    for ind, value in enumerate(primes):
        if value is True:
            primes[ind*2::ind] = [False] * (((number - 1)//ind)-1)
            primes_list.append(ind)
        if value is False and ind % 2 != 0:
            composite_numbers.append(ind)
    return primes_list, composite_numbers[2:]

def refute_goldback_conjecture(upper_bound):
    primes, composite_numbers = eratosthenes_sieve(upper_bound)
    squares = [x ** 2 for x in range(1,1000000)]
    squares_set = set(squares)
    result_composites = set()
    composite_numbers_set = set(composite_numbers)
    for composite in composite_numbers:
        for prime in primes:
            square = int((composite - prime)/2)
            if square in squares_set and square >= 1 and square % 1 == 0:
                result_composites.add(composite)
                square_root = math.sqrt(square)
                break
    return min(composite_numbers_set.difference(result_composites))

def main():
    blurb()
    start = time.time()
    RESULT = refute_goldback_conjecture(10000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
