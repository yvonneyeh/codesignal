# def adjacentElementsProduct(inputArray):
#
#     # inputArray = [3, 6, -2, -5, 7, 3]
#     # 3, 6 ... 6, -2 ... -2, -5 ....... 7, 3
#
#     # in = [3, 5]
#     # out = 15
#
#     # in = []
#     # output = None
#
#
#
#     # 1. check every item in the list
#     # 2. keep track of which 2 items in a row  make largest product
#     # 3. creating new list that will keep track of current 2 items
#     # 4. check if next 2 items create larger product
#     # 5. keep track of current largest product
#
#
#     largest_product = 0
#
#     for i in range((len(inputArray)-1)):
#         new_product = (inputArray[i] * inputArray[i+1])
#         print(new_product)
#         if new_product < largest_product:
#             continue
#         else:
#             # new_product > largest_product:
#             print('hi')
#             largest_product = new_product
#             print(f'largest = {largest_product}')
#             print(f'new = {new_product}')
#         # else:
#         #     continue
#     return largest_product


def adjacentElementsProduct(inputArray):

    largest_product = inputArray[-1] * inputArray[-2]

    for i in range((len(inputArray)-1)):
        new_product = inputArray[i] * inputArray[i+1]
        if largest_product > new_product:
        if new_product > largest_product:
            largest_product = new_product

    return largest_product


inputArray = [-23, 4, -3, 8, -12]
# [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(inputArray))
