#!/usr/bin/env python3
import time
import math

def blurb():
  print("""

Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41

is clearly divisible by 41.

The incredible formula n2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n2+an+b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

  """)

def eratosthenes_sieve(number):
    primes = [True] * number
    primes[0], primes[1] = [False] * 2
    primes_list = []
    for ind, value in enumerate(primes):
        if value is True:
            primes[ind*2::ind] = [False] * (((number - 1)//ind)-1)
            primes_list.append(ind)
    return primes_list

def quadratic_function_finder():
    quadratic_function = lambda n, a, b: n**2 + a * n + b
    a_range = range(-1000, 1001)
    b_range = range(1, 1001)
    primes_under_million = set(eratosthenes_sieve(1000000))
    n_max = a_max = b_max = 0
    for a_number in a_range:
        for b_number in b_range:
            n = 1
            while quadratic_function(n, a_number, b_number) in primes_under_million:
                n+=1
                if n > n_max:
                    n_max = n
                    a_max = a_number
                    b_max = b_number
    product = a_max * b_max
    RESULT = "a: %d, b: %d, longest sequence: %d, product: %d" % (a_max, b_max, n_max, product)
    return RESULT

def main():
  start = time.time()
  RESULT = quadratic_function_finder()
  end   = time.time() - start
  print("Result: %s"      % RESULT)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
