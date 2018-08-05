#!/usr/bin/env python3
import time

def blurb():
    print("""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
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
        sequential_digits = set(range(1,max(digit_set) + 1))
        difference_between_seq_and_set = sequential_digits.difference(digit_set)
        if len(difference_between_seq_and_set) == 0:
            return True
    return False

def find_longest_pandigital_prime():
    primes = eratosthenes_sieve(9876543)
    result = 0
    for prime in primes:
        if is_pandigital(prime, check_sequential=True):
            if prime > result:
                result = prime
    return result

def main():
    blurb()
    start = time.time()
    RESULT = find_longest_pandigital_prime()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
