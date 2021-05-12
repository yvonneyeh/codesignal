# An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
# Given a string, find out if it satisfies the IPv4 address naming rules.

def isIPv4Address1(inputString):

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

# Pass 18/21 tests

def isIPv4Address(inputString):

    # Make a regular expression
    # for validating an Ip-address
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, inputString)):
        return True

    else:
        return False
    
