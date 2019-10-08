def oddTuples(aTup):
    aList = []
    for i in range (0,len(aTup)):
        if i % 2 == 0:
            aList.append(aTup[i])
        else:
            continue
    return(tuple(aList))
