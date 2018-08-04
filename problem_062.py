#!/usr/bin/env python3
import collections
import time


def blurb():
    print("""
    The cube, 41063625 (3453), can be permuted to produce two other cubes:
    56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
    which has exactly three permutations of its digits which are also cube.

    Find the smallest cube for which exactly five permutations of its digits are
    cube.
    """)


def return_five_repeats(test_list, repeat):
    '''
    In a given list, return the items that are repeated <repeat> times
    '''
    count = {}
    for key, item in enumerate(test_list):
        if item not in count.keys():
            count[item] = []
        count[item].append(key)
        if len(count[item]) == 5:
            return count[item]


def problem_062():
    '''
    Create a huge list of cubes, use another method to try and find 5 equal
    permutations
    '''
    upper_range = 9999
    cubed = lambda x: ''.join(sorted(str(x ** 3)))
    cubes_list = [cubed(x) for x in range(upper_range)]
    repeats = return_five_repeats(cubes_list, 5)
    print("Found the cubes of %s have the same digits..." % str(repeats))
    return min(repeats) ** 3


def main():
    blurb()
    start = time.time()
    RESULT = problem_062()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
