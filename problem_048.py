#!/usr/bin/env python3
import time


def blurb():
    print("""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """)


def find_last_digits_of_series(upper_bound):
    upper_bound += 1
    find_series = [x ** x for x in range(1,upper_bound)]
    find_series = sum(find_series)
    series_str = str(find_series)
    series_str_len = len(series_str)
    return series_str[series_str_len - 10:]


def main():
    blurb()
    start = time.time()
    RESULT = find_last_digits_of_series(1000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
