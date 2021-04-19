#Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

def firstNotRepeatingCharacter(s):

    # look at every letter in string
    # add all letters to a dictionary to keep track of count
    # increment by one every time you see char
    # loop through 2nd time
    # if total is 1, return it

    dict = {}

    for letter in s:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1

    for i in range(len(s)):
        if dict[s[i]] == 1:
            return s[i]

    return '_'


# Time: 11:23
