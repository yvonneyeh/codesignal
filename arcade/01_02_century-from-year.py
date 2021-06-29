def centuryFromYear(year):

    # if 1 <= year < 101:
    #     return 1
    # elif 101 <= year <= 200:
    #     return 2
    # elif 201 <= year <= 300:
    #     return 3
    # 1601 <= year <= 1700
    # 2001 <= year <= 2005:
    # return 21

    # test cases:
    # i = 1
    # o = 1

    # i = 100
    # o = 1

    # i = 101
    # o = 2

    # if year in range(1,100):


    x = year/100
    # print(x)
    if x <= year <= (101*x):
        if year == 1:
            return 1
            # print(a)
        if year % 100 == 0:
            return int(x)
            # print(b)
        if year % 10 != 0:
            return int(x)+1
            # print(c)
        else:
            return int(x)
    # if 101 <= year <= 200:

    # # if 2001 <= year <= 2005:
    # #     return 21
