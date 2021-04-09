# Given two strings, find the number of common characters between them.

def commonCharacterCount(s1, s2):

    # two strings, return output int count of common chars
    # turn one string into list
    # iterate through list and check if letter in other word exists
    # remove letter

    count = 0
    list2 = list(s2)

    for letter in s1:
        if letter in list2:
            list2.remove(letter)
            count += 1
    return count
