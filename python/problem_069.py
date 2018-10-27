#!/usr/bin/env python3
import time


def blurb():
    print("""
    Euler's Totient function, φ(n) [sometimes called the phi function], is used
    to determine the number of numbers less than n which are relatively prime to
    n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
    relatively prime to nine, φ(9)=6.

    n   Relatively Prime    φ(n)    n/φ(n)
    2   1                   1        2
    3   1,2                 2        1.5
    4   1,3                 2        2
    5   1,2,3,4             4        1.25
    6   1,5                 2        3
    7   1,2,3,4,5,6         6        1.1666...
    8   1,3,5,7             4        2
    9   1,2,4,5,7,8         6        1.5
    10  1,3,7,9             4        2.5

    It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

    Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
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


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def get_numbers(upper_bound, numbers = [1]):
    '''
    get the factorials of primes below the upper_bound
    '''
    primes = eratosthenes_sieve(100)
    for i in range(1, 101):
        if max(numbers) > upper_bound:
            numbers.pop()
            break
        product = 1
        for item in primes[:i]:
            product *= item
        numbers.append(product)
    return numbers


def list_of_totient_numbers(upper_bound):
    '''
    Loop through all numbers calculating the totient number to return a
    dictionary of integers to the totient number
    Only do factorials of primes to save time
    '''
    totient_numbers = {}
    numbers = get_numbers(upper_bound)
    for i in numbers:
        totient_numbers[i] = 0
        for j in range(1, i + 1):
            if gcd(j, i) == 1:
                totient_numbers[i] += 1
    return totient_numbers


def problem_069(upper_bound):
    totient_numbers = list_of_totient_numbers(upper_bound)
    max_n_over_phi = 0
    for integer, totient in totient_numbers.items():
        i_over_t = integer / totient
        if i_over_t > max_n_over_phi:
            result = integer
            max_n_over_phi = i_over_t
    return result


def main():
    blurb()
    start = time.time()
    RESULT = problem_069(1000000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
