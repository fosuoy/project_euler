#!/usr/bin/env python3
import time

def blurb():
    print("""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
    """)

def find_palindromes(upper_bound):
    reverse = lambda x: x[::-1]
    upper_bound += 1
    results = []
    for number in range(1,upper_bound):
        number_str = str(number)
        if reverse(number_str) == number_str:
            binary = str(bin(number))[2:]
            if reverse(binary) == binary:
                print(number)
                results.append(number)
    return sum(results)

def main():
    blurb()
    start = time.time()
    RESULT = find_palindromes(1000000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
