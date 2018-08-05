#!/usr/bin/python
# Lattice paths
# https://projecteuler.net/problem=15
# Disclosure, script appropriated / influenced from here:
# http://code.jasonbhill.com/python/project-euler-problem-15/
# Not suitable for the full 20, 20 grid solution

import time
 
 
grid = [2,2]
 
def Path(grid):
    if grid == [0,0]:
        return 1
    counter = 0
    if grid[0] > 0:
        counter += Path([grid[0]-1,grid[1]])
    if grid[1] > 0:
        counter += Path([grid[0],grid[1]-1])
    return counter
 
start = time.time()
result = Path(grid)
elapsed = time.time() - start
 
print "result %s found in %s seconds" % (result, elapsed)
