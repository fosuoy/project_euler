#!/usr/bin/env python3
import time


def blurb():
    print("""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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


def find_consecutive_primes():
    primes = eratosthenes_sieve(1000000)
    primes_set = set(primes)
    result_count_start = 0
    result_count_end = 0
    running_list = 0
    result_sum = 0
    number_gen = [x for x in range(0,1000)]
    for number_s in number_gen:
        for number_e in number_gen:
            current_sum = sum(primes[number_s:number_e])
            current_list = number_e - number_s
            if current_list > running_list and current_sum in primes_set:
                running_list = current_list
                result_sum = current_sum
                result_count_start = number_s
                result_count_end = number_e
    return "prime[ %d ] to prime[ %d ] = %d" % \
            (result_count_start, result_count_end, result_sum)


def main():
    blurb()
    start = time.time()
    RESULT = find_consecutive_primes()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
