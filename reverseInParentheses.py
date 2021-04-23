# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

def reverseInParentheses(inputString):

    # look at all characters
    # add everything within () into a stack
    # pop items from stack into new string
    stack = []
    for x in inputString:
        if x ==")":
            temp =""
            while stack[-1] !="(":
                temp += stack.pop()
            stack.pop() # pop the (
            for item in temp:
                stack.append(item)
        else:
            stack.append(x)

    return"".join(stack)


def reverseInParentheses_1Line(inputString):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


def reverseInParentheses_Recursive(inputString):
    for i in range(len(inputString)):
        if inputString[i] == '(':
            start = i
        if inputString[i] == ')':
            end = i
            return reverseInParentheses(inputString[:start]+inputString[end-1:start:-1]+inputString[end+1:])
    return inputString
