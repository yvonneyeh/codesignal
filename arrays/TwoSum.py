# You have two integer arrays, a and b, and an integer target value v.
# Determine whether there is a pair of numbers,
# where one number is taken from a and the other from b,
# that can be added together to get a sum of v.
# Return true if such a pair exists, otherwise return false.

def sumOfTwo(a, b, v):

    # input = 2 lists, value
    # output = boolean

    # look at every number in list a
    # subtract num from target value to find next values
    # turn list b into a set for easy checking of existence of next value
    # if num exists in set b there is a pair!

    difference = []
    b_set = set(b)

    for num in a:
        new_num = v - num
        difference.append(new_num)

    for num in difference:
        if num in b_set:
            return True
    return False
