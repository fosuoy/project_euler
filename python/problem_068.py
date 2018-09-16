#!/usr/bin/env python3
import itertools
import time


def blurb():
    print("""
    Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
    and each line adding to nine.

    Working clockwise, and starting from the group of three with the numerically
    lowest external node (4,3,2 in this example), each solution can be described
    uniquely. For example, the above solution can be described by the set:
    4,3,2; 6,2,1; 5,1,3.

    It is possible to complete the ring with four different totals: 9, 10, 11,
    and 12. There are eight solutions in total.
    Total   Solution Set
    9   4,2,3; 5,3,1; 6,1,2
    9   4,3,2; 6,2,1; 5,1,3
    10  2,3,5; 4,5,1; 6,1,3
    10  2,5,3; 6,3,1; 4,1,5
    11  1,4,6; 3,6,2; 5,2,4
    11  1,6,4; 5,4,2; 3,2,6
    12  1,5,6; 2,6,4; 3,4,5
    12  1,6,5; 3,5,4; 2,4,6

    By concatenating each group it is possible to form 9-digit strings; the
    maximum string for a 3-gon ring is 432621513.

    Using the numbers 1 to 10, and depending on arrangements, it is possible to
    form 16- and 17-digit strings. What is the maximum 16-digit string for a
    "magic" 5-gon ring?
    """)


def is_valid_gon_ring(gon_ring):
    '''
    Refer to problem_068 for format of gon_ring
    10-6 should be in outer ring
    1-5 should be in inner ring
    '''
    outer = [gon_ring[0], gon_ring[3], gon_ring[5], gon_ring[8], gon_ring[9]]
    inner = [gon_ring[1], gon_ring[2], gon_ring[4], gon_ring[6], gon_ring[7]]
    outer_expected = set([10, 9, 8, 7, 6])
    if outer_expected != set(outer):
        return False
    sum_one = sum([gon_ring[0], gon_ring[1], gon_ring[4]])
    sum_two = sum([gon_ring[3], gon_ring[4], gon_ring[7]])
    sum_thr = sum([gon_ring[5], gon_ring[2], gon_ring[1]])
    sum_fou = sum([gon_ring[8], gon_ring[7], gon_ring[6]])
    sum_fiv = sum([gon_ring[9], gon_ring[6], gon_ring[2]])
    if len(set([sum_one, sum_two, sum_thr, sum_fou, sum_fiv])) != 1:
        return False
    return True


def find_gon_rings(result = []):
    '''
    Similar to the below, loop over all permutations and find valid gon_rings
    '''
    result = 0
    permutations = [x for x in itertools.permutations(range(1, 11), 10)]
    for p in permutations:
        if is_valid_gon_ring(p):
            gon_ring_list = []
            gon_ring_list.append([p[0], p[1], p[4]])
            gon_ring_list.append([p[3], p[4], p[7]])
            gon_ring_list.append([p[5], p[2], p[1]])
            gon_ring_list.append([p[8], p[7], p[6]])
            gon_ring_list.append([p[9], p[6], p[2]])
            gon_ring_list.sort()
            gon_ring_string = ''
            for gon_ring in gon_ring_list:
                for item in gon_ring:
                    gon_ring_string += str(item)
            gon_ring_int = int(gon_ring_string)
            if gon_ring_int >= result:
                result = gon_ring_int
    return result


def problem_068():
    '''
    The gon ring will be represented by a 10 digit array:
        0
         |  3
          1
        2   4
      5 |  |
         6-7-8
         9
    ==
    [0,1,2,3,4,5,6,7,8,9]
    Where:
    10-6 must exist in the the outer ring
    1-5 must exist in the inner ring
    '''
    gon_rings = find_gon_rings()
    return gon_rings


def main():
    blurb()
    start = time.time()
    RESULT = problem_068()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
