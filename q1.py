def getPrimeNumbers(n):
    """Takes an integer parameter.
    
        Returns a list of prime numbers up to the parameter.
    """
    result = []
    startNum = 2;
    for i in range(startNum, n+1):
        if isPrimeNumber(i):
            result.append(i)
    return result

def isPrimeNumber(n):
    """Takes an integer parameter.
        Returns true or false if parameter is a prime number.
    """

    # base cases
    if (n == 2 or n == 3):
        return True
    else:
        # check for factors
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True

number = 100
print("Prime numbers up to " + str(number))
print(getPrimeNumbers(number))