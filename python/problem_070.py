#!/usr/bin/env python3
import time


def blurb():
    print("""
    Euler's Totient function, φ(n) [sometimes called the phi function], is used
    to determine the number of positive numbers less than or equal to n which
    are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
    less than nine and relatively prime to nine, φ(9)=6.
    The number 1 is considered to be relatively prime to every positive number,
    so φ(1)=1.

    Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
    permutation of 79180.

    Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and
    the ratio n/φ(n) produces a minimum.
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


def list_of_totient_numbers(upper_bound):
    '''
    Loop through all numbers calculating the totient number to return a
    dictionary of integers to the totient number
    '''
    totient_numbers = {}
    primes = eratosthenes_sieve(5000)
    for i in primes:
        for j in primes:
            if j <= i: continue
            n = i * j
            if n > upper_bound: continue
            else:
                phi = (i - 1) * (j - 1)
                if same_integers(n, phi):
                    print('phi(%d) = %d' % (n, phi))
                    totient_numbers[n] = phi
    return totient_numbers


def integer_to_dict(integer):
    '''
    Converts an integer to a dictionary of the integer and the number of times
    it appears in the number
    '''
    results = {}
    for number in str(integer):
        if number not in results.keys():
            results[number] = 0
        results[number] += 1
    return results


def same_integers(a, b):
    '''
    Simple check to make sure the same integers in one number are the same in
    another
    '''
    if integer_to_dict(a) == integer_to_dict(b):
        return True
    else:
        return False


def problem_070(upper_bound):
    '''
    Given a map of n to phi - calculate 1 / phi for each number, return the
    minimum n
    '''
    totient_numbers = list_of_totient_numbers(upper_bound)
    min_n_over_phi = 1000000
    for integer, totient in totient_numbers.items():
        if same_integers(integer, totient):
            i_over_t = integer / totient
            if i_over_t < min_n_over_phi:
                min_n_over_phi = i_over_t
                result = integer
    return result


def main():
    blurb()
    start = time.time()
    RESULT = problem_070(10000000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
