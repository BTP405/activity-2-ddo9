def printStats(t):
    """Takes a file name as a parameter.

        Reads the numbers from a file and for each line calls
        a decorator function.
    """
    file = open(t, "r")
    numberLine = []
    lineNum = 0
    for line in file:
        lineNum += 1
        for number in line.split():
            numberLine.append(int(number))
        decorator(numberLine, lineNum)
        numberLine = []
    file.close()

def decorator(n, l):
    """Displays the numbers, count, average and max from a given list of numbers.

    Keyword arguments:
    n -- the list of numbers on a line of a file
    l -- the line number associated with the list
    """
    numbersRead = n
    numbersCount = len(numbersRead)
    numbersAvg = sum(numbersRead) / numbersCount
    numbersMax = max(numbersRead)
    print("Line Number: " + str(l))
    print("Numbers read: ", end="") #, end="" is to prevent a newline 
    print(numbersRead)
    print("Numbers Counted: " + str(numbersCount))
    print("Average of Numbers: " + str(numbersAvg))
    print("Maximum of Numbers: " + str(numbersMax))
    print("")

fileName = "numbers.txt"
print("Reading file \"" + fileName + "\"")
printStats(fileName)