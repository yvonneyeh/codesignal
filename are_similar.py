def areSimilar(a, b):

    count=0
    swap=[]

    if set(a) != set(b):
        return False

    for i in range(len(a)):
        if a[i] not in b:
            return False
        elif a[i] != b[i]:
            count+=1
            swap.append([a[i],b[i]])
            if count>2:
                return False
    if count ==0 or count ==2 and swap[0]==swap[1][::-1]:
        return True
    else:
        return False
