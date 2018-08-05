#!/usr/bin/env python3
import time


def blurb():
    print("""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
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


def find_prime_value_family(upper_limit):
    primes = eratosthenes_sieve(upper_limit)
    primes = [x for x in primes if x > 999]
    primes_set = set(primes)
    primes_strings = [str(x) for x in primes]
    count_r = 0
    prime_fam = []
    five_digit_positions = [
            [2,3],
            [1,2],
            [0,1],
            [0,2],
            [0,3],
            [1,3],
            ]
    six_digit_positions = [
            [0,2,3],
            [0,2,4],
            [0,1,2],
            [0,3,4],
            [2,3,4],
            [1,2,4],
            [0,1,4],
            [1,3,4],
            [0,1,3],
            [1,2,3],
            ]
    for prime_string in primes_strings:
        count = 0
        prime_family = set()
        if len(prime_string) > 5:
            positions = six_digit_positions
        else:
            positions = five_digit_positions
        for position in positions:
            count = 0
            prime_family = set()
            prime_string_list = list(prime_string)
            for replacement in '0123456789':
                for item in position:
                    prime_string_list[item] = replacement
                prime_test = int("".join(prime_string_list))
                if prime_test in primes_set:
                    count += 1
                    prime_family.add(prime_test)
            if count > count_r:
                count_r = count
                prime_fam = prime_family
    for item in prime_fam: print(item)
    return min(prime_fam)


def main():
    blurb()
    start = time.time()
    RESULT = find_prime_value_family(1000000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
