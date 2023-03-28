import sys


def getDataFile(path):
    fd = open(path, 'r')
    return fd.read()


def getFileSystem(buffer):
    path = "."
    lsIsRunning = False
    osDict = {}

    for x in buffer:
        if x[0] == '$':
            if lsIsRunning:
                lsIsRunning = False
            command = x[2:].split(' ')
            if command[0] == "cd":
                if command[1] == "..":
                    path = path[:path.rfind('/')]
                elif command[1] == "/":
                    path = "."
                else:
                    path += "/" + command[1]
            elif command[0] == "ls":
                lsIsRunning = True
                osDict[path] = []
        else:
            file = x.split(' ')
            if file[0] == "dir":
                osDict[path].append(path + "/" + file[1])
            else:
                osDict[path].append(int(file[0]))
    return osDict


def getDirectorySize(osDict, path):
    size = 0
    for x in osDict[path]:
        if type(x) != int:
            size += getDirectorySize(osDict, x)
        else:
            size += x
    return size


def getSum(osDict):
    osDictSize = {}
    directorys = {}

    for x in osDict.keys():
        osDictSize[x] = getDirectorySize(osDict, x)
    for x in osDictSize.keys():
        if osDictSize[x] <= 100000:
            directorys[x] = osDictSize[x]
    total = 0
    for x in directorys.keys():
        total += directorys[x]
    return total


def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        lines = buffer.split('\n')
        osDict = getFileSystem(lines)
        print(getSum(osDict))
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)


if __name__ == "__main__":
    main()
