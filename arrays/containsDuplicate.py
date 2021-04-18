def containsDuplicates(a):

    # loop through all numbers
    # add numbers to a set
    # if the number is already in the set return true
    # if you get to the end of the function return false

    a_set = set()
    for num in a:
        if num not in a_set:
            a_set.add(num)
        else:
            return True
    return False
