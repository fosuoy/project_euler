#!/usr/bin/env python3
import time


def blurb():
    print("""
    A googol (10100) is a massive number: one followed by one-hundred zeros;
    100100 is almost unimaginably large: one followed by two-hundred zeros.
    Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, ab, where a, b < 100, what is the
    maximum digital sum?
    """)


def get_digital_sum(number):
    digital_sum = 0
    number_str = str(number)
    for digit in number_str:
        digital_sum += int(digit)
    return digital_sum


def get_max_sum_of_digits_in_powers(upper_bound):
    max_sum = 0
    mid_point = upper_bound // 2
    result = {}
    for a in range(1, upper_bound + 1):
        for b in range(1, upper_bound + 1):
            digital_sum = get_digital_sum(a ** b)
            if digital_sum > max_sum:
                result['a'] = a
                result['b'] = b
                result['digital_sum'] = digital_sum
                max_sum = digital_sum
    print('{} ** {} = {}'.format(
        result['a'], result['b'], result['digital_sum']))
    return str(max_sum)


def main():
    blurb()
    start = time.time()
    RESULT = get_max_sum_of_digits_in_powers(100)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
