def quicksort(array,lo,hi):
    if lo < hi:
        boundary1,boundary2 = dutch_national_flag_partition(array,lo,hi)
        quicksort(array,lo,boundary1-1)
        quicksort(array,boundary2+1,hi)
    return array

def dutch_national_flag_partition(array,lo,hi):
    '''
    In place

    Stable Because there is a condition to check if there are there are the same elements
    '''
    j = lo + 1
    pivot = array[lo]
    while j <= hi:
        #Red case
        if array[j] < pivot:
            array[j],array[lo] = array[lo], array[j]
            lo += 1
            j += 1
        #White Case
        elif array[j] == pivot:
            j += 1
        #Blue Case
        else:
            array[j],array[hi] = array[hi],array[j]
            hi -= 1
    return lo,hi

array = [8,5,8,15,1,13,11,8,6,11,3,2]
lo = 0
hi = len(array)-1
print(quicksort(array,lo,hi))
