def firstDuplicate(a):

    # check every number
    # add all numbers to a new set
    # if number doesn't exist return it

    a_set = set()
    for num in a:
        if num not in a_set:
            a_set.add(num)
            print(a_set)
        elif num in a_set:
            return num
    return -1
