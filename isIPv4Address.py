def isIPv4Address(inputString):

    numbers = inputString.split('.')
    print(numbers)
    try:
        for i in numbers:
            print(i)
            if len(numbers)!= 4:
                return False
            else:
                if i == None:
                    return False
                else:
                    num = int(i)
                    if num < 0 or num > 255:
                        return False
    except ValueError:
        return False
    return True
