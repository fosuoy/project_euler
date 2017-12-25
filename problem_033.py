#!/usr/bin/env python3
import time
from fractions import Fraction

def blurb():
    print("""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    """)

def denominator_value_curious_fractions():
    '''
    for all numbers between 10 and 99 inclusive if the digit of the numerator
    is equivalent to the ten of the denominator, see if 
    '''
    numerators = range(10,100)
    denominators = range(10,100)
    result = 1
    for numerator in numerators:
        for denominator in denominators:
            if numerator < denominator:
                numerator_digit = numerator % 10
                denominator_digit = denominator // 10
                if numerator_digit == denominator_digit:
                    simplified_n, simplified_d = \
                            int((numerator - numerator_digit) / 10), \
                            int(denominator - (denominator_digit * 10))
                    if simplified_n < simplified_d:
                        simplified_frac = simplified_n / simplified_d
                        test_frac = numerator / denominator
                        if simplified_frac == test_frac:
                            print("%d / %d == %d / %d" % 
                                    (simplified_n, simplified_d, numerator, denominator))
                            result *= Fraction(simplified_n, simplified_d)
    return result

def main():
    blurb()
    start = time.time()
    RESULT = denominator_value_curious_fractions()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
