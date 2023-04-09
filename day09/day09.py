import sys


def getDataFile(path):
    fd = open(path, 'r')
    return fd.read()

def getInstructions(lines):
    instructions = []
    
    for x in lines:
        tmp = x.split(' ')
        instructions.append((tmp[0], int(tmp[1])))
    return instructions

def updateTails(headPosition, tailPosition):
    yDiff = headPosition[0] - tailPosition[0]
    xDiff = headPosition[1] - tailPosition[1]
    
    if xDiff == 0 and yDiff == 2:
        tailPosition[0] += 1
    elif xDiff == 1 and yDiff == 2:
        tailPosition[0] += 1
        tailPosition[1] += 1
    elif xDiff == 2 and yDiff == 1:
        tailPosition[0] += 1
        tailPosition[1] += 1
    elif xDiff == 2 and yDiff == 0:
        tailPosition[1] += 1
    elif xDiff == 2 and yDiff == -1:
        tailPosition[0] -= 1
        tailPosition[1] += 1
    elif xDiff == 1 and yDiff == -2:
        tailPosition[0] -= 1
        tailPosition[1] += 1
    elif xDiff == 0 and yDiff == -2:
        tailPosition[0] -= 1
    elif xDiff == -1 and yDiff == -2:
        tailPosition[0] -= 1
        tailPosition[1] -= 1
    elif xDiff == -2 and yDiff == -1:
        tailPosition[0] -= 1
        tailPosition[1] -= 1
    elif xDiff == -2 and yDiff == 0:
        tailPosition[1] -= 1
    elif xDiff == -2 and yDiff == 1:
        tailPosition[0] += 1
        tailPosition[1] -= 1
    elif xDiff == -1 and yDiff == 2:
        tailPosition[0] += 1
        tailPosition[1] -= 1

def moveRight(positionsVisited, n, headPosition, tailPosition):
    for _ in range(n):
        headPosition[1] += 1
        updateTails(headPosition, tailPosition)
        positionsVisited[(tailPosition[0], tailPosition[1])] = True

def moveLeft(positionsVisited, n, headPosition, tailPosition):
    for _ in range(n):
        headPosition[1] -= 1
        updateTails(headPosition, tailPosition)
        positionsVisited[(tailPosition[0], tailPosition[1])] = True

def moveUp(positionsVisited, n, headPosition, tailPosition):
    for _ in range(n):
        headPosition[0] += 1
        updateTails(headPosition, tailPosition)
        positionsVisited[(tailPosition[0], tailPosition[1])] = True

def moveDown(positionsVisited, n, headPosition, tailPosition):
    for _ in range(n):
        headPosition[0] -= 1
        updateTails(headPosition, tailPosition)
        positionsVisited[(tailPosition[0], tailPosition[1])] = True

def simulateRopes(instructions):
    headPosition = [0, 0]
    tailPosition = [0, 0]
    positionsVisited = {}

    for x in instructions:
        print("==", x[0], x[1], "==")
        if x[0] == 'R':
            moveRight(positionsVisited ,x[1], headPosition, tailPosition)
        elif x[0] == 'L':
            moveLeft(positionsVisited, x[1], headPosition, tailPosition)
        elif x[0] == 'U':
            moveUp(positionsVisited, x[1], headPosition, tailPosition)
        elif x[0] == 'D':
            moveDown(positionsVisited, x[1], headPosition, tailPosition)
    print(len(positionsVisited))

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        lines = buffer.split('\n')
        instructions = getInstructions(lines)
        simulateRopes(instructions)
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)


if __name__ == "__main__":
    main()