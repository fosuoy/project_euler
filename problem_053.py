#!/usr/bin/env python3
import time


def blurb():
    print("""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr = 	
n!
r!(n−r)!
	,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
    """)


def find_combinations_over_million():
    ftl = lambda x: x * ftl(x - 1) if x > 1 else 1
    combinatoric = lambda n, r: int(ftl(n) / (ftl(r) * ftl(n - r)))
    results = []
    for n in range(1,101):
        for r in range(1,n):
            if combinatoric(n, r) > 1000000:
                results.append({"n": n, "r": r})
    return len(results)


def main():
    blurb()
    start = time.time()
    RESULT = find_combinations_over_million()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
