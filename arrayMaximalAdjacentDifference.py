# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

def arrayMaximalAdjacentDifference(inputArray):
    a = inputArray
    max_a = abs(a[0]-a[1])
    for i in range(len(a)-1):
        if abs(a[i]-a[i+1]) > max_a:
            max_a = abs(a[i]-a[i+1])
    return max_a
