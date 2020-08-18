def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        #left, pivot, right = naive_partition(array)
        left, pivot, right = naive_partition_stable(array)
        return quicksort(left) + pivot + quicksort(right)

def naive_partition(array):
    pivot = array[0]
    left = []
    right = []
    
    for i in range(1,len(array)):
        if array[i] <= pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    return left,[pivot],right
    
def naive_partition_stable(array):
    pivot = array[0]
    left = []
    right = []
    pivots = [pivot]
    
    for i in range(1,len(array)):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] == pivot:
            pivots.append(array[i])
        else:
            right.append(array[i])
    return left,pivots,right
    
array = [8,5,8,15,1,13,11,8,6]
print(quicksort(array))
