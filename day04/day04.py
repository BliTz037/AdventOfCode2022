import sys

def getDataFile(path):
    fd = open(path, 'r')
    return fd.read()

def getSectionAssignmentPair(buffer):
    bufferArray = buffer.split('\n')
    sections = []
    
    for x in bufferArray:
        pairs = x.split(',')
        elfsPair = []
        for y in pairs:
            section = y.split('-')
            elfsPair.append((int(section[0]), int(section[1])))
        sections.append(elfsPair)
    return sections

def getPairsContainOther(sections):
    i = 0
    for x in sections:
        if (x[0][0] <= x[1][0]) and (x[0][1] >= x[1][1]):
            i += 1
        elif (x[1][0] <= x[0][0]) and (x[1][1] >= x[0][1]):
            i += 1
        else:
            continue
    return i

def getPairsOverlap(sections):
    i = 0
    for x in sections:
        if (x[0][0] <= x[1][0]) and (x[0][1] >= x[1][1]):
            i += 1
        elif (x[1][0] <= x[0][0]) and (x[1][1] >= x[0][1]):
            i += 1
        elif (x[0][0] <= x[1][1]) and (x[0][1] >= x[1][0]):
            i += 1
        else:
            continue
    return i

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        sections = getSectionAssignmentPair(buffer)
        print(getPairsContainOther(sections))
        print(getPairsOverlap(sections))
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)

if __name__ == "__main__":
    main()
