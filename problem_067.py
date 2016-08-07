#!/usr/bin/python
# Maximum path sum II
# https://projecteuler.net/problem=67
# Largest sum of attached number triangle

import time

# Transforms data in txt file into list where each row is a list.
table = [map(int, n.split()) for n in open('problem_067.txt').readlines()]

start = time.time()
LENGTH = len(table)

# Start counting from the bottom of the pyramid
# Starting from the bottom of the pyramid, the maximum of two numbers next
# to each other are summed with the number above them both.
# By the time it get's to the top of the pyramid, the maximum number that can
# be summed is returned.
for row in range(LENGTH - 1, 0, -1):
  for column in range(0, row):
    table[row-1][column] += max(table[row][column], table[row][column + 1])
result = table[0][0]
elapsed = time.time() - start
 
print("Result %s found in %s seconds" % (result, elapsed))
