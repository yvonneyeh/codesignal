def binary_search(lst, value):

    # set a min and max Index
    # check if guess is what your looking for value is - if so stop
    # if not, set a guess as median of min & max (if not int, round down)
    # if guess is smaller, reset max
    # if guess is larger, reset min
    # compute a new guess, then restart

    min = 0
    max = len(lst)-1

    while min <= max:
        guess = (min + max)//2
        if lst[guess] > value:
            max = guess - 1
        elif lst[guess] < value:
            min = guess + 1
        else:
            return guess
    return -1
