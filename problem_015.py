#!/usr/bin/python
# Lattice paths
# https://projecteuler.net/problem=15
# Disclosure, script appropriated from here:
# http://code.jasonbhill.com/python/project-euler-problem-15/
# Not suitable for the full 20, 20 grid solution

import time
 
 
grid = [2,2]
 
def recPath(gridSize):
    if gridSize == [0,0]:
        return 1
    counter = 0
    if gridSize[0] > 0:
        counter += recPath([gridSize[0]-1,gridSize[1]])
    if gridSize[1] > 0:
        counter += recPath([gridSize[0],gridSize[1]-1])
 
    return paths
 
start = time.time()
result = recPath(gridSize)
elapsed = time.time() - start
 
print "result %s found in %s seconds" % (result, elapsed)
