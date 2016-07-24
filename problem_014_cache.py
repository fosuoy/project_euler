#!/usr/bin/python
# Solution to Project Euler problem 14
# https://projecteuler.net/problem=14
# Similar to other solution but with a 'cache' implemented
# A dictionary holding the solutions to each step from 1-1,000,000 is kept
# Lowers time taken from ~1 minute + to ~3.5s

import time

collatz_e = lambda x: x / 2
collatz_o = lambda x: (3 * x) + 1

max_steps = 0
start = 0
cache={}

start_time = time.time()

for number in range(1,1000000):
    counter = 1
    start = number
    while number > 1:
        if (start - 1) > number:
            counter += cache[number]
            break
        elif (number % 2) == 0:
            number = collatz_e(number)
            counter = counter + 1
        else:
            number = collatz_o(number)
            counter = counter + 1
    if counter > max_steps:
        max_steps = counter
        max_start = start
    cache[start] = (counter - 1)

end_time = time.time() - start_time

print("Start: %s  Steps: %s  Time: %s" % (max_start, max_steps, end_time))
