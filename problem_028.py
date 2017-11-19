#!/usr/bin/env python3

def create_number_block( blockSize ):
    if blockSize % 2 == 0:
        return ['Not an odd number...']

    initalLine = list( [None] * blockSize )
    spiral = []
    for i in range(blockSize):
        spiral.append(list(initalLine))
    
    return spiral


def number_spiral( spiral, blockSize ):
    midPointX = midPointY = int((blockSize / 2))
    X = Y = blockSize
    x = y = 0
    dx = 0
    dy = -1
    for i in range(1, max(X, Y)**2 + 1):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            coOrdinateX = midPointX + x
            coOrdinateY = midPointY + y
            spiral[coOrdinateY][coOrdinateX] = i
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    return spiral


def count_diagnals( spiral ):
    x = 0
    result = 0
    midPoint = int(len(spiral) / 2)
    for i in range(0, len(spiral)):
        line = spiral[i]

        if i < midPoint:
            lineLength = len(line) -1
            result += line[x] + line[lineLength - x]
            x += 1
            continue
        if i == midPoint:
            result += line[x]
            x -= 1
            continue
        if i > midPoint:
            lineLength = len(line) - 1
            result += line[x] + line[lineLength - x]
            x -= 1
            continue
    return result


def main():
    blockSize = 1001
    numberSpiral = create_number_block(blockSize)
    numberSpiral = number_spiral(numberSpiral, blockSize)
    result = count_diagnals( numberSpiral )
    print(result)

if __name__ == '__main__':
    main()
