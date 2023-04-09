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
    changes = {
        (2, 1):(1, 1),
        (1, 2):(1, 1),
        (2, 0):(1, 0),
        (2, -1):(1, -1),
        (1, -2):(1, -1),
        (0, -2):(0, -1),
        (-1, -2):(-1,-1),
        (-2, -1):(-1, -1),
        (-2, 0):(-1, 0),
        (-2, 1):(-1, 1),
        (-1, 2):(-1, 1),
        (0, 2):(0, 1),
        # Part 2
        (2, 2):(1, 1),
        (-2, -2):(-1, -1),
        (-2, 2):(-1, 1),
        (2, -2):(1, -1)
      }

    if (yDiff, xDiff) in changes:
        tailPosition[0] += changes[(yDiff, xDiff)][0]
        tailPosition[1] += changes[(yDiff, xDiff)][1]

def simulateRopes(instructions):
    headPosition = [0, 0]
    tailPosition = [0, 0]
    positionsVisited = {}

    for x in instructions:
        #print("==", x[0], x[1], "==")
        for _ in range(x[1]):
            if x[0] == 'R':
                headPosition[1] += 1
            elif x[0] == 'L':
                headPosition[1] -= 1
            elif x[0] == 'U':
                headPosition[0] += 1
            elif x[0] == 'D':
                headPosition[0] -= 1
            updateTails(headPosition, tailPosition)
            positionsVisited[(tailPosition[0], tailPosition[1])] = True
    print(len(positionsVisited))


def simulateRopes2(instructions):
    headPosition = [0, 0]
    positionsVisited = {}  # Last tails
    tails = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
             [0, 0], [0, 0], [0, 0], [0, 0]
             ]
    for x in instructions:
        #print("==", x[0], x[1], "==")
        for _ in range(x[1]):
            if x[0] == 'R':
                headPosition[1] += 1
            elif x[0] == 'L':
                headPosition[1] -= 1
            elif x[0] == 'U':
                headPosition[0] += 1
            elif x[0] == 'D':
                headPosition[0] -= 1
            updateTails(headPosition, tails[0])
            for i in range(1, len(tails)):
                updateTails(tails[i-1], tails[i])
            positionsVisited[(tails[-1][0], tails[-1][1])] = True
    print(len(positionsVisited))


def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        lines = buffer.split('\n')
        instructions = getInstructions(lines)
        simulateRopes(instructions)
        simulateRopes2(instructions)
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)


if __name__ == "__main__":
    main()