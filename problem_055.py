#!/usr/bin/env python3
import time


def blurb():
    print("""
            If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

            Not all numbers produce palindromes so quickly. For example,

            349 + 943 = 1292,
            1292 + 2921 = 4213
            4213 + 3124 = 7337

            That is, 349 took three iterations to arrive at a palindrome.

            Although no one has proved it yet, it is thought that some numbers,
            like 196, never produce a palindrome. A number that never forms a
            palindrome through the reverse and add process is called a Lychrel
            number. Due to the theoretical nature of these numbers, and for the
            purpose of this problem, we shall assume that a number is Lychrel
            until proven otherwise. In addition you are given that for every
            number below ten-thousand, it will either (i) become a palindrome in
            less than fifty iterations, or, (ii) no one, with all the computing
            power that exists, has managed so far to map it to a palindrome. In
            fact, 10677 is the first number to be shown to require over fifty
            iterations before producing a palindrome:
            4668731596684224866951378664 (53 iterations, 28-digits).

            Surprisingly, there are palindromic numbers that are themselves
            Lychrel numbers; the first example is 4994.

            How many Lychrel numbers are there below ten-thousand?

            NOTE: Wording was modified slightly on 24 April 2007 to emphasise
            the theoretical nature of Lychrel numbers.
    """)


def is_lychrel_number(number):
    '''
    If a palindrome is reached, stop, it is not a lychrel number.
    '''
    palindrome = lambda x: str(x) == str(x)[::-1]
    reverse = lambda x: int(str(x)[::-1])

    for _ in range(50):
        number = number + reverse(number)
        if palindrome(number):
            return False
    return True


def no_of_lychrel_numbers(upper_bound):
    '''
    Count number of lychrel numbers below an upper bound
    '''
    result = 0
    for number in range(10, upper_bound + 1):
        if is_lychrel_number(number): result += 1
    return result


def main():
    blurb()
    start = time.time()
    RESULT = no_of_lychrel_numbers(10000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
