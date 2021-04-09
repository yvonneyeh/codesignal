# Given an array of strings, return another array containing all of its longest strings.

def allLongestStrings(inputArray):

    # longest variable to keep track of current longest, start with none
    # loop through the list to check every word
    # if length of word is longest than current longest, set to longest
    # variable should be a list, append long items

    # longest = [0]

    # for i in range(len(inputArray)-1):
    #     if len(inputArray[i]) > len(longest[0]):
    #         longest.pop(i)
    #         longest.append(inputArray[i])
    #     elif len(inputArray[i]) == len(longest[0]):
    #         longest.append(inputArray[i])
    #     return longest

    longest = 0

    for i in range(0,len(inputArray)):
        longest = max(longest,len(inputArray[i]))

    return [i for i in inputArray if len(i) == longest]


# For inputArray = ["aba", "aa", "ad", "vcd", "aba"]
# output = allLongestStrings(inputArray) = ["aba", "vcd", "aba"]
