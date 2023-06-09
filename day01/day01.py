import sys

def getDataFile(path):
    fd = open(path, 'r')
    return fd.read()

def getElfsInventory(buffer):
    bufferArray = buffer.split('\n')
    elfsInventory = []    
    numberTabTmp = []
    
    for x in bufferArray:
        if len(x) == 0:
            elfsInventory.append(numberTabTmp.copy())
            numberTabTmp.clear()
            continue
        try:
            numberTabTmp.append(int(x))
        except ValueError as e:
            raise e
    return elfsInventory

def calcElfsCalories(elfsInventory):
    totalElfsCalories = []
    tmp = 0
    
    for y in elfsInventory:
        for x in y:
            tmp += x
        totalElfsCalories.append(tmp)
        tmp = 0
    return totalElfsCalories

def findBigCalories(elfsCalories):
    maxValue = (0, 0)

    for x in enumerate(elfsCalories):
        if x[1] > maxValue[1]:
            maxValue = x
    return maxValue

def sumCalories(elfsCalories, nbElfs):
    total = 0

    for x in range(nbElfs):
        bigCalories = findBigCalories(elfsCalories)
        total += bigCalories[1]
        del elfsCalories[bigCalories[0]]
    return total

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        bufferArray = getElfsInventory(buffer)
        totalElfsCalories = calcElfsCalories(bufferArray)
        print("The elf carrying the most calories has", findBigCalories(totalElfsCalories)[1], "calories")
        print("The 3 elfs carrying the most calories have", sumCalories(totalElfsCalories, 3), "calories")
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)
    except ValueError as e:
        print("Parse failed !", e)
        sys.exit(1)
    except Exception as e:
        print("Unknown error !", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
