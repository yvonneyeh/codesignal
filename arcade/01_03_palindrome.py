def checkPalindrome(inputString):

    half = (len(inputString)//2)
    # print(half)

    if len(inputString) == 1:
        return True
    for i in range(half):
        # print(i)
        if inputString[i] != inputString[-(i+1)]:
            return False
    return True

def isPalindrome(inputString):
    print(inputString[::-1])
    return inputString == inputString[::-1]

inputString = 'racecarq'
# checkPalindrome(inputString)
isPalindrome(inputString)
