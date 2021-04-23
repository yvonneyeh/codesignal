def reverseInParentheses(inputString):

    # look at all characters
    # add everything within () into a stack
    # pop items from stack into new string
    pass

def reverseInParentheses_Recursive(inputString):
    for i in range(len(inputString)):
        if inputString[i] == '(':
            start = i
        if inputString[i] == ')':
            end = i
            return reverseInParentheses(inputString[:start]+inputString[end-1:start:-1]+inputString[end+1:])
    return inputString
