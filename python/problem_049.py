#!/usr/bin/env python3
import time
import itertools


def blurb():
    print("""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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


def group_permutations(primes):
    prime_strings = [str(x) for x in primes]
    results = []
    checked = set()
    for prime in prime_strings:
        if prime not in checked:
            checked.add(prime)
            groups = set()
            groups.add(prime)
            permutations = itertools.permutations(prime)
            found = False
            for permutation in permutations:
                permutation = ''.join(permutation)
                checked.add(permutation)
                if permutation in prime_strings:
                    groups.add(permutation)
                    found = True
            if found:
                if len(groups) >= 3:
                    groups = [int(x) for x in groups]
                    groups.sort()
                    results.append(list(groups))
    return results


def find_arithmetic_sequence():
    primes = set(eratosthenes_sieve(10000))
    primes_10 = set(eratosthenes_sieve(10))
    primes = [x for x in primes if x > 1000]
    prime_groups = group_permutations(primes)
    groups = []
    results = []
    for group in prime_groups:
        for prime in group:
            for other_prime in group:
                if prime != other_prime and prime > other_prime:
                    flag = False
                    remainder = prime - other_prime
                    if prime + remainder in group: flag = True
                    if flag:
                        groups = set()
                        for prime in group:
                            if prime + remainder in group:
                                groups.add(prime)
                                groups.add(prime + remainder)
                        results.append(list(groups))
                        break
    print("Primes which display described properties:")
    for result in results:
        print(result)
        if 1487 not in result:
            prime_group = [str(x) for x in result]
            prime_group = ''.join(prime_group)
    return prime_group


def main():
    blurb()
    start = time.time()
    RESULT = find_arithmetic_sequence()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
