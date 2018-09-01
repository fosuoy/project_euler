#!/usr/bin/env python3
import decimal
import fractions
import math
import time


def blurb():
    print("""
    Consider quadratic Diophantine equations of the form:

    x2 – Dy2 = 1

    For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

    It can be assumed that there are no solutions in positive integers when D is
    square.

    By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
    following:

    32 – 2×22 = 1
    22 – 3×12 = 1
    92 – 5×42 = 1
    52 – 6×22 = 1
    82 – 7×32 = 1

    Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
    obtained when D=5.

    Find the value of D ≤ 1000 in minimal solutions of x for which the largest
    value of x is obtained.
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


def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    if x != 0:
        while x * x != apositiveint:
            x = (x + (apositiveint // x)) // 2
            if x in seen: return False
            seen.add(x)
    return True


def chakravala_recurse(n, k, a, b, m0, m = None):
    if m == None:
        m = m0
    diff = (m + m0) % abs(k)
    m_lo = m0 - diff
    m_hi = m_lo + abs(k)
    m = m_hi if abs(m_hi * m_hi - n) < abs(m_lo * m_lo - n) else m_lo
    a_new = ((a * m) + (n * b)) / abs(k)
    b_new = (a + (b * m)) / abs(k)
    k_new = (m * m - n) // k
    if k_new == 1:
        a_result = math.pow(a_new, 2) + n * math.pow(b_new, 2)
        b_result = 2 * a_new * b_new
        return a_new, b_new
    elif k_new in [-1, -2, 2, -4, 4]:
        if abs(k_new) == 4 and not ((a_new % 1) or (b_new % 1)):
            return chakravala_recurse(n, k_new, a_new, b_new, m0, m)
        else:
            a_result = (math.pow(a_new, 2) + (n * math.pow(b_new, 2))) // abs(k_new)
            b_result = (2 * a_new * b_new) / abs(k_new)
            return a_result, b_result
    else:
        return chakravala_recurse(n, k_new, a_new, b_new, m0, m)


def chakravala_method(n, a=None, b=1, k=-1):
    '''
    a^2 - n * b ^2 = k
    a^2 = k + n * b^2
    Assuming b = 1,
    x = sqrt(k + n)
    for any k integer to achieve an X integer
    See examples here:
    https://en.wikipedia.org/wiki/Chakravala_method
    '''
    y_k = n + k
    if a == None: a = int(math.sqrt(y_k))
    while not is_square(y_k):
        k -= 1
        y_k = n + k
    m0 = int(math.sqrt(n))
    a, b = chakravala_recurse(n, k, a, b, m0)
    return a, b


def problem_066(upper_bound):
    x_max = 0
    D_max = 0
    primes = eratosthenes_sieve(upper_bound)
    solve = lambda x,d,y: (math.pow(x, 2)) - (d * (math.pow(y, 2)))
    for D in primes:
        x, y = chakravala_method(D)
        if x and x > x_max:
            x_max = x
            y_max = y
            D_max = D
    print("%d ^ 2 - %d * %d ^ 2 = 1" % (x_max, D_max, y_max))
    return D_max


def main():
    blurb()
    start = time.time()
    RESULT = problem_066(1000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
