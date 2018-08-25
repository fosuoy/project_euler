#!/usr/bin/env python3
import time


def blurb():
    print("""
    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and
    'Save Link/Target As...'), a 15K text file containing a triangle with
    one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not
    possible to try every route to solve this problem, as there are 299
    altogether! If you could check one trillion (1012) routes every second
    it would take over twenty billion years to check them all. There is an
    efficient algorithm to solve it. ;o)
    """)


def problem_067():
    # Transforms data in txt file into list where each row is a list.
    with open('problem_067.txt', 'r') as f:
        file_contents = f.read()
    split_table = lambda x: [int(a) for a in x.split(' ') if a != '']
    file_contents = file_contents.split('\n')
    table = [split_table(x) for x in file_contents]
    table.pop()
    table_len = len(table)

    # Start counting from the bottom of the pyramid
    # Starting from the bottom of the pyramid, the maximum of two numbers next
    # to each other are summed with the number above them both.
    # By the time it get's to the top of the pyramid, the maximum number that can
    # be summed is returned.
    for row in range(table_len - 1, 0, -1):
        for column in range(0, row):
            number = max(table[row][column], table[row][column + 1])
            table[row-1][column] += number
    return table[0][0]
     

def main():
    blurb()
    start = time.time()
    RESULT = problem_067()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
