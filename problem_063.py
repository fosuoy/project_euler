#!/usr/bin/env python3
import itertools
import time


def blurb():
    print("""
    The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
    number, 134217728=8^9, is a ninth power.

    How many n-digit positive integers exist which are also an nth power?
    """)


def return_power_generator(power, power_len):
    for digit in itertools.count(start=1, step=1):
        result = digit ** power
        result_len = len(str(result))
        if result_len < power_len:
            continue
        if result_len > power_len:
            break
        yield digit ** power


def problem_063():
    nth_powers = 0
    for power in itertools.count(start=1, step=1):
        power_generator = return_power_generator(power, power)
        results = False
        for item in power_generator:
            results = True
            nth_powers += 1
        if results == False:
            break
    return nth_powers


def main():
    blurb()
    start = time.time()
    RESULT = problem_063()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
