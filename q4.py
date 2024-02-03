def printStats(t):
    file = open(t, "r")
    numberLine = []
    lineNum = 0
    for line in file:
        lineNum += 1
        # reading each word        
        for number in line.split():
            numberLine.append(int(number))
        decorator(numberLine, lineNum)
        numberLine = []
    file.close()

def decorator(n, l):
    numbersRead = n
    numbersCount = len(numbersRead)
    numbersAvg = sum(numbersRead) / numbersCount
    numbersMax = max(numbersRead)
    print("Line Number: " + str(l))
    print("Numbers read: ", end="")
    print(numbersRead)
    print("Numbers Counted: " + str(numbersCount))
    print("Average of Numbers: " + str(numbersAvg))
    print("Maximum of Numbers: " + str(numbersMax))
    print("")

printStats("numbers.txt")