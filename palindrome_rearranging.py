# Given a string, find out if its characters can be rearranged to form a palindrome.

def palindromeRearranging1(inputString):

    # return (len(inputString) / 2 ) == len(set(inputString))

    # passes 6/10 tests

    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

    # passes 10/10 tests

def palindromeRearranging(inputString):

    counted_str=[]
    done=[]
    for i in inputString:
        if i in done:
            continue
        if inputString.count(i)%2==1:
            counted_str.append(inputString.count(i))
            done.append(i)
    if len(counted_str)>1:
        return False
    else:
        return True
