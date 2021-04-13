# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
#
# Given a ticket number n, determine if it's lucky or not.

def isLucky(n):

    # read the ticket number
    # divide ticket number in half
        # half of length of N
    # get sum of first half and second half
    # return true if same, false if not

    #   string = str(n)
    # top = [int(x) for x in string[:len(string)//2]]
    # bottom = [int(x) for x in string[len(string)//2:]]
    # return sum(top) == sum(bottom)

    ticket = str(n)
    half = len(ticket)//2
    front = [int(x) for x in ticket[:half]]
    back = [int(x) for x in ticket[half:]]
    # print(front)
    # print(back)

    return sum(front) == sum(back)
