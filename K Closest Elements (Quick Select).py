def quickselect(array,lo,hi,k):
    if hi > lo:
        pivot = array[lo]
        mid = partition(array,lo,hi,pivot)
        #Checks if the kth position is less than mid, if yes, recurse left of the array
        if k < mid:
            return quickselect(array,lo,mid-1,k)
        #Checks if the kth position is more than mid, if yes, recurse right of the array
        elif k > mid:
            return quickselect(array,mid+1,hi,k)
        else:
            return array[k]
    else:
        return array[k]

def partition(array,start,end,pivot):
    index = start
    for i in range(start+1,end+1):
        if array[i] < pivot:
            index += 1
            array[index],array[i] = array[i],array[index]

    array[start],array[index] = array[index],array[start]
    return index

def k_closest_numbers(array,lo,hi,k):
    result = [None] * k
    mid = (lo + hi) // 2
    median = quickselect(array,lo,hi,mid) #Complexity is O(n)
    absolute_list = [(abs(elem - median),elem) for elem in array] #Complexity is O(n)

    #Note apparently in comparison for tuples, only the first element in the tuple is compared
    #E.g. (1,5) > (2,3) is 1 > 2, False
    #     (7,1) > (5,9) is 7 > 5, True
    
    #This will sort the list into smallest difference first
    quickselect(absolute_list,lo,hi,mid) #Complexity is O(n)
    for i in range(k):
        result[i] = absolute_list[i+1][1]
    return result,median
    
array = [11,3,10,16,5,4,1,20,6,18,7,8]
lo = 0
hi = len(array)-1
k = 4
print(k_closest_numbers(array,lo,hi,4))
