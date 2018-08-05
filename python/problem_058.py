#!/usr/bin/env python3
import time

from math import sqrt


def blurb():
    print("""
            Starting with 1 and spiralling anticlockwise in the following way, a
            square spiral with side length 7 is formed.

            37 36 35 34 33 32 31
            38 17 16 15 14 13 30
            39 18  5  4  3 12 29
            40 19  6  1  2 11 28
            41 20  7  8  9 10 27
            42 21 22 23 24 25 26
            43 44 45 46 47 48 49

            It is interesting to note that the odd squares lie along the bottom
            right diagonal, but what is more interesting is that 8 out of the 13
            numbers lying along both diagonals are prime; that is, a ratio of
            8/13 ≈ 62%.

            If one complete new layer is wrapped around the spiral above, a
            square spiral with side length 9 will be formed. If this process is
            continued, what is the side length of the square spiral for which
            the ratio of primes along both diagonals first falls below 10%?
    """)


def is_prime(n):
    '''
    Method to tell if a number is prime or not, returns True / False
    '''
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def generate_spiral_corners():
    '''
    Generator to return next corner when given a maximum corner
    e.g.
    [3, 5, 7, 9],
    [13, 17, 21, 25],
    -31, 37, 43, 49]...
    '''
    first_corner = 1
    current_difference = 2
    current_corner = first_corner
    while current_corner > 0:
        corners = []
        for i in range(4):
            current_corner += current_difference
            corners.append(current_corner)
        current_difference += 2
        yield corners


def problem_058():
    '''
    The solution to problem 058
    '''
    spiral_size = 7
    ratio_of_primes = 1
    number_of_primes, counter = 0, 0
    for item in generate_spiral_corners():
        item.pop()
        counter += 1
        sides = 2 * counter + 1
        for number in item:
            if is_prime(number):
                number_of_primes += 1
        total_diagonals = 4 * counter + 1
        primes_ratio = number_of_primes / total_diagonals
        if primes_ratio < 0.1:
            result = sides
            break
    return result


def main():
    blurb()
    start = time.time()
    RESULT = problem_058()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
