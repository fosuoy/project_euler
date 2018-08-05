#!/usr/bin/env python3
import time

from fractions import Fraction


def blurb():
    print("""
            It is possible to show that the square root of two can be expressed
            as an infinite continued fraction.

            √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

            By expanding this for the first four iterations, we get:

            1 + 1/2 = 3/2 = 1.5
            1 + 1/(2 + 1/2) = 7/5 = 1.4
            1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
            1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

            The next three expansions are 99/70, 239/169, and 577/408, but the
            eighth expansion, 1393/985, is the first example where the number of
            digits in the numerator exceeds the number of digits in the
            denominator.

            In the first one-thousand expansions, how many fractions contain a
            numerator with more digits than denominator?
    """)


def get_continued_fractions(upper_bound):
    '''
    Recurse to upper bound continued fraction
    '''
    result = 0
    fraction = 1 + Fraction(1, 2)

    for _ in range(upper_bound):
        num_digits = len(str(fraction.numerator))
        den_digits = len(str(fraction.denominator))
        if num_digits > den_digits:
            print("Iteration {} : {}".format(_ + 1, fraction))
            result += 1
        fraction = 1 + Fraction(1, 1 + fraction)
    return result

def main():
    blurb()
    start = time.time()
    RESULT = get_continued_fractions(1000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
