import sys

def getDataFile(path):
    fd = open(path, 'r')
    return fd.read()

def getStackCrates(buffer):
    bufferArray = buffer.split('\n')
    
    for idx, x in enumerate(bufferArray):
        if len(x) == 0:
            return bufferArray[:idx]
    return []

def getInstructions(buffer):
    bufferArray = buffer.split('\n')
    
    for idx, x in enumerate(bufferArray):
        if len(x) == 0:
            return bufferArray[idx + 1:]
    return []

def parseStackCrates(stack):
    idxLenLastLine = len(stack) - 1
    stacksParsed = []

    for x in stack[idxLenLastLine]:
        if x != ' ':
            stacksParsed.append([])
    for x in range(0, idxLenLastLine):
        i = 0
        y = 0
        while i < len(stack[x]):
            if stack[x][i] == '[':
                stacksParsed[y].append(stack[x][i + 1])
            i += 4
            y += 1
    return stacksParsed

def parseIntructions(instructions):
    instructionsParsed = []

    for x in instructions:
        instructionsParsed.append(x.split(' '))
    return instructionsParsed

def doRearrangement(stacks, instructions):
    
    for instruction in instructions:
        loopNb = int(instruction[1])
        fromIdx = int(instruction[3]) - 1
        toIdx = int(instruction[5]) - 1
        for x in range(loopNb):
            stacks[toIdx].insert(0, stacks[fromIdx].pop(0))
    return stacks

def doRearrangementCrateMover9001(stacks, instructions):
    for instruction in instructions:
        loopNb = int(instruction[1])
        fromIdx = int(instruction[3]) - 1
        toIdx = int(instruction[5]) - 1
        
        stacks[toIdx] = stacks[fromIdx][:loopNb] + stacks[toIdx]
        stacks[fromIdx] = stacks[fromIdx][loopNb:]
    return stacks

def getMessage(stacks):
    message = ""
    for x in stacks:
        message += x[0]
    return message

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        stackParsed = parseStackCrates(getStackCrates(buffer))
        instructionsParsed = parseIntructions(getInstructions(buffer))
        #newStack = doRearrangement(stackParsed, instructionsParsed)
        print(stackParsed)
        newStack2 = doRearrangementCrateMover9001(stackParsed, instructionsParsed)
        #print(getMessage(newStack))
        print(getMessage(newStack2))
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)

if __name__ == "__main__":
    main()
