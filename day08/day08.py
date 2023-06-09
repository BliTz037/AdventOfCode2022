import sys


def getDataFile(path):
    fd = open(path, 'r')
    return fd.read()

# PART ONE

def getTreeVisible(buffer):
    columnsLen = len(buffer[0])
    rowLen = len(buffer)
    treeVisible = 0

    for y in range(0, rowLen):
        for x in range(0, columnsLen):
            if (isLeftVisible(buffer, x, y) == True or isRightVisible(buffer, x, y) == True or isUpVisible(buffer, x, y) == True or isDownVisible(buffer, x, y) == True):
                treeVisible += 1
                # print("Tree visible", (y,x))
                continue            
    return treeVisible 

def isLeftVisible(buffer, x, y):
    for i in range(x - 1, -1, -1):
        if (buffer[y][x] <= buffer[y][i]):
            return False
    return True

def isRightVisible(buffer, x, y):
    columnsLen = len(buffer[0])
    for i in range(x + 1, columnsLen):
        if (buffer[y][x] <= buffer[y][i]):
            return False
    return True

def isUpVisible(buffer, x, y):
    for i in range(y - 1, -1, -1):
        if (buffer[y][x] <= buffer[i][x]):
            return False
    return True

def isDownVisible(buffer, x, y):
    rowLen = len(buffer)
    for i in range(y + 1, rowLen):
        if (buffer[y][x] <= buffer[i][x]):
            return False
    return True

# PART TWO

def getUpTreeVisible(buffer, x, y):
    tmp = 0
    for i in range(y - 1, -1, -1):
        tmp += 1
        if (buffer[y][x] <= buffer[i][x]):
            break
    return tmp

def getLeftTreeVisible(buffer, x, y):
    tmp = 0
    for i in range(x - 1, -1, -1):
        tmp += 1
        if (buffer[y][x] <= buffer[y][i]):
            break
    return tmp

def getRightTreeVisible(buffer, x, y):
    columnsLen = len(buffer[0])
    tmp = 0
    for i in range(x + 1, columnsLen):
        tmp += 1
        if (buffer[y][x] <= buffer[y][i]):
            break
    return tmp

def getDownTreeVisible(buffer, x, y):
    rowLen = len(buffer[0])
    tmp = 0
    for i in range(y + 1, rowLen):
        tmp += 1
        if (buffer[y][x] <= buffer[i][x]):
            break
    return tmp

def getHighestScenicValue(buffer):
    columnsLen = len(buffer[0])
    rowLen = len(buffer)
    treeVisible = 0

    for y in range(0, rowLen):
        for x in range(0, columnsLen):
            upTree = getUpTreeVisible(buffer, x, y)
            leftTree = getLeftTreeVisible(buffer, x, y)
            rightTree = getRightTreeVisible(buffer, x, y)
            downTree = getDownTreeVisible(buffer, x, y)
            tmp = upTree * leftTree * rightTree * downTree
            if (tmp > treeVisible):
                treeVisible = tmp
            #print("Tree visible", (y,x), ":", tmp)
    return treeVisible

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        lines = buffer.split('\n')
        print(getTreeVisible(lines))
        print("Highest scenic value:", getHighestScenicValue(lines))
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)


if __name__ == "__main__":
    main()
