def isPrime(n):
    divider = 2
    while (divider < n):
        if(n % divider == 0):
            return False
        divider += 1
    return True


def isPalindrome(n):
    stringN = str(n)
    if(stringN == stringN[::-1]):
        return True
    return False


for i in reversed(list(range(2, 1001))):
    if isPrime(i) and isPalindrome(i):
        print(i)
        break
