#!/usr/bin/env python3
import time

def blurb():
    print("""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    """)

def find_irrational_fraction():
    string_together = lambda x: "".join([str(y) for y in range(1,x)])
    fraction = string_together(1000000)
    required_fractions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    result = 1
    for number in required_fractions:
        number -= 1
        dn = int(fraction[number])
        result *= dn
    return result

def main():
    blurb()
    start = time.time()
    RESULT = find_irrational_fraction()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
