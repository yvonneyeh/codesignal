# Given a string, find out if its characters can be rearranged to form a palindrome.

def palindromeRearranging(inputString):

    return (len(inputString) / 2 ) == len(set(inputString))

    # passes 6/10 tests
