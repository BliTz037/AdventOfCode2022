import sys

def getDataFile(path):
    fd = open(path, 'r')
    return fd.read()

def isFirstMarker(marker):
    x = 0
    i = 1
    while x != len(marker):
        while i != len(marker):
            if marker[i] == marker[x] and i != x:
                #print(marker[i], marker[x], marker)
                return False
            i += 1
        x += 1
        i = 1
    return True

def findStartPacket(buffer, size):
    for idx, x in enumerate(buffer):
        tmp = buffer[idx: idx + size]
        if (len(tmp) != size):
            break
        if (isFirstMarker(tmp) == True):
            return ((tmp, idx + size))
        #print(tmp)
    return None

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        test = findStartPacket(buffer, 4)
        test = findStartPacket(buffer, 14)
        print(test)
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)

if __name__ == "__main__":
    main()
