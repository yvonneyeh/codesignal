def avoidObstacles(inputArray):

    jumps = 2

    while True:
        if sorted([i%jumps for i in inputArray])[0] > 0:
            return jumps
        jumps += 1


def avoidObstaclesTesting(inputArray):

    # sort inputArray
    # check mod

    obstacles = sorted(inputArray)
    jumps = 1
    print(inputArray)
    print(obstacles)
    print([i%jumps for i in inputArray])
    for i in obstacles:
        print(i)
    print(sorted([i%jumps for i in inputArray]))

    while True:
        if sorted([i%jumps for i in inputArray])[0] > 0:
            return jumps
        jumps += 1
