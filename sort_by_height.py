def sortByHeight(a):

    # keep trees where they are
    # move only people
    # create a new list of only people
    # sort people List
    # replace sorted people with people in full list

    people = sorted([x for x in a if x != -1])
    # print(people)
    # print(sorted(people))

    j = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = people[j]
            j += 1
    return a


# Time: 34:14
