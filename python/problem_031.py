#!/usr/bin/env python3
import time


def blurb():
    print("""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
    """)


def find_combination(total):
    '''
    Was stuck here, read through this persons implementation before doing the
    below:
    http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
    '''
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    results = [0] * ( total + 1 )
    results[0] = 1
    for denomination in range(0, len(coins)):
        for coin in range(coins[denomination], total + 1):
            results[coin] += results[coin - coins[denomination]]
    return results[total]


def main():
    blurb()
    start = time.time()
    RESULT = find_combination(200)
    end = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
