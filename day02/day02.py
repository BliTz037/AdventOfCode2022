import sys

def getDataFile(path):
    fd = open(path, 'r')
    return fd.read()

def getOutcomRound(choice):
    if choice[0] == 'A':
        if choice[1] == 'X':
            return 3
        elif choice[1] == 'Y':
            return 6
        else:
            return 0
    elif choice[0] == 'B':
        if choice[1] == 'Y':
            return 3
        elif choice[1] == 'Z':
            return 6
        else:
            return 0
    else:
        if choice[1] == 'Z':
            return 3
        elif choice[1] == 'X':
            return 6
        else:
            return 0

def getMatchStrategies(choice):
    if choice[0] == 'A':
        if choice[1] == 'X':
            return 'Z'
        elif choice[1] == 'Y':
            return 'X'
        else:
            return 'Y'

    elif choice[0] == 'B':
        if choice[1] == 'X':
            return 'X'
        elif choice[1] == 'Y':
            return 'Y'
        else:
            return 'Z'
    else:
        if choice[1] == 'X':
            return 'Y'
        elif choice[1] == 'Y':
            return 'Z'
        else:
            return 'X'

def getShapeScore(shape):
    return 1 if shape == 'X' else 2 if shape == 'Y' else 3

def getMatchScore(match, elfStrategy):
    choice = match.split(' ')
    if elfStrategy:
        choice[1] = getMatchStrategies(choice)
    return getOutcomRound(choice) + getShapeScore(choice[1])

def getAllScore(buffer, elfStrategy):
    bufferArray = buffer.split('\n')
    scores = []
    for x in bufferArray:
        scores.append(getMatchScore(x, elfStrategy))
    return scores

def getMyScore(scores):
    myScore = 0
    for x in scores:
        myScore += x
    return myScore

# AX Rock 1 | BY Paper 2 | CZ Scissors 3
# Lose 0 | Draw 3 | Win 6 

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        buffer = getDataFile(sys.argv[1])
        scores = getAllScore(buffer, False)
        print("Your total score will be", getMyScore(scores))
        
        scores = getAllScore(buffer, True)
        print("Your total score with strategy guide will be", getMyScore(scores))
    except OSError:
        print("Impossible to read", sys.argv[1])
        sys.exit(1)
    except Exception as e:
        print("Unknown error !", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
