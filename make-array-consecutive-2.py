# Make Array Consecutive 2!

def makeArrayConsecutive2(statues):

# test
# statues = [6, 2, 3, 8]
# makeArrayConsecutive2(statues) = 3
# 2, 3, _ , _ , 6, _ , 8

# 1. sort the statute list
# 2. look at every item in the list
# 3. counter, keep track of where you are in the list
# 4. counter = first item in sorted list = current number
# 5. if the next item in the list is not +1 of previous item
# 6. insert item at index +1
# 7. increment counter and the index

    statues.sort()
    count = 0

    for i in range(len(statues)-1):
        current = statues[i]
        next_item = statues[i+1]
        if next_item - current > 1:
            count += next_item - current - 1
    return count
