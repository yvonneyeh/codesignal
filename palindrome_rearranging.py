# Given a string, find out if its characters can be rearranged to form a palindrome.

def palindromeRearranging(inputString):

    # return (len(inputString) / 2 ) == len(set(inputString))

    # passes 6/10 tests

    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

    # passes 10/10 tests
