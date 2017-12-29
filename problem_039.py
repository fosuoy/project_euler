#!/usr/bin/env python3
import time
import math

def blurb():
    print("""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
    """)

def find_solutions_for_triangle(number, powers, power_set):
    upper_bound = number - 2
    results = []
    middle_bound = upper_bound // 2
    quarter_bound = middle_bound // 2
    test_range_lower = range(1, quarter_bound)
    test_range_high = range(quarter_bound, middle_bound)
    for a in test_range_lower:
        for b in test_range_high:
            a_2 = powers[a]
            b_2 = powers[b]
            c_2 = a_2 + b_2
            if c_2 in power_set:
                c = powers.index(c_2)
                if a + b + c == number:
                    results.append([a, b, c])
    return results

def find_most_results_for_range(upper_bound):
    upper_bound += 1
    powers_list = [x ** 2 for x in range(0,upper_bound)]
    power_set = set(powers_list)
    result = 0
    result_length = 0
    test_range = [x for x in range(1, upper_bound)]
    for number in test_range:
        solutions = find_solutions_for_triangle(number, powers_list, power_set)
        if len(solutions) > result_length:
            result = number
            result_length = len(solutions)
            print(str(number) + ":")
            print(solutions)
    return result

def main():
    '''
    Speed is:
    Result: 840
    Completed in 282.286678314209

    '''
    blurb()
    start = time.time()
    RESULT = find_most_results_for_range(1000)
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
