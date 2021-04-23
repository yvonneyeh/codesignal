# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def addBorder(picture):

    border = ['*'*(len(picture[0])+2)]
    for i in picture:
        border.append('*'+i+'*')
    border.append(border[0])

    return border
