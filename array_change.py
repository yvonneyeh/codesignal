# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

def arrayChange(inputArray):
    a=0
    newArray = inputArray[:]
    for i in range(len(inputArray)-1):
        if newArray[i] >= newArray[i+1]:
            a += newArray[i] - newArray[i+1]+1
            newArray[i+1] = newArray[i]+1
    return a
