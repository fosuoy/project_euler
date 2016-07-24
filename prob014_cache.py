#!/usr/bin/python

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
