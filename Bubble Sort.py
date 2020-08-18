array = [7,8,5,4,7,9,2,4]

def bubbleSort(aList):
    n=len(aList)
    for i in range(n):
        for j in range(n-1):
            if aList[j]>aList[j+1]:
               aList[j],aList[j+1] = aList[j+1],aList[j] 
    return aList

print(bubbleSort(array))

def betterbubbleSort(aList):
    n=len(aList)
    for i in range(n):
        for j in range((n-1)-i):
            if aList[j]>aList[j+1]:
               aList[j],aList[j+1] = aList[j+1],aList[j] 
    return aList

print(betterbubbleSort(array))
