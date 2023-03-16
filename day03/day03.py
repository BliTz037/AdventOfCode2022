import sys


def getDataFile(path):
    fd = open(path, 'r')
    return fd.read()

def findSameItem(bag):
    for x in range(len(bag[0])):
        tmp = bag[0][x]
        for y in range(len(bag[0])):
            if tmp == bag[1][y]:
                return bag[0][x]
    return ('')

def findBadge(team):
    bagCheck = team[1:]
    for x in team[0]:
        if bagCheck[0].find(x) != -1 and bagCheck[1].find(x) != -1:
            return x
    return ''

def getPriorities(item):
    
    if item == '':
        return 0
    if item.isupper():
        return ord(item) - ord('A') + 1 + 26
    else:
        return ord(item) - ord('a') + 1

def getSumPriorities(buffer):
    bufferArray = buffer.split('\n')
    total = 0

    for x in bufferArray:
        arrLen = len(x)
        bag = (x[:arrLen//2], x[arrLen//2:])
        item = findSameItem(bag)
        total += getPriorities(item)
    return total

def getSumBadgePriorities(buffer):
    bufferArray = buffer.split('\n')
    total = 0
    i = 0
    
    while i < len(bufferArray):
        team = [bufferArray[i], bufferArray[i + 1], bufferArray[i + 2]]
        badge = findBadge(team)
        total += getPriorities(badge)
        i = i + 3
    return total

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        print(getSumPriorities(buffer))
        print(getSumBadgePriorities(buffer))
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)
    except Exception as e:
        print("Unknown error !", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
