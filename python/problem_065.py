#!/usr/bin/env python3
import decimal
import fractions
import math
import time


def blurb():
    print("""
    The square root of 2 can be written as an infinite continued fraction.

    √2 = 1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / (...))))

    The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
    that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

    It turns out that the sequence of partial values of continued fractions for
    square roots provide the best rational approximations. Let us consider the
    convergents for √2.

    Hence the sequence of the first ten convergents for √2 are:
    1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

    What is most surprising is that the important mathematical constant,
    e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

    The first ten terms in the sequence of convergents for e are:
    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

    The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

    Find the sum of digits in the numerator of the 100th convergent of the
    continued fraction for e.
    """)


def get_convergents(no_convergents):
    '''
    The pattern of convergents for e is:
     2 - 1 - 2 - 1 - 1 - 4 - 1 - 1 - 6 - 1 - 1  - 8...
    [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11]
    '''
    convergent_list = [2, 1, 2]
    count = len(convergent_list)
    convergents_pattern = 2
    while len(convergent_list) < no_convergents:
        if count % 3 == 2:
            convergents_pattern += 2
            convergent_list.append(convergents_pattern)
        else:
            convergent_list.append(1)
        count += 1
    return convergent_list


def get_convergent_term(convergents):
    '''
    Given a list of convergents, run through it multiplying current position and
    adding previous position (the pattern for finding numerators of convergent
    fractions of e)
    '''
    previous_numerator = 2
    current_numerator = 3
    convergents.pop(0)
    convergents.pop(0)
    while len(convergents) > 0:
        p_n = current_numerator
        multiplier = convergents.pop(0)
        current_numerator *= multiplier
        current_numerator += previous_numerator
        previous_numerator = p_n
    return current_numerator


def problem_065(no_convergents):
    convergents = get_convergents(no_convergents)
    return sum([int(x) for x in str(get_convergent_term(convergents))])


def main():
    blurb()
    start = time.time()
    RESULT = problem_065(100)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
