def getPrimeNumbers(n):
    result = []
    startNum = 2;
    for i in range(startNum, n+1):
        if isPrimeNumber(i):
            result.append(i)
    return result

def isPrimeNumber(n):
    if (n == 2 or n == 3):
        return True
    else:
        # check for factors
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    
print(getPrimeNumbers(100))