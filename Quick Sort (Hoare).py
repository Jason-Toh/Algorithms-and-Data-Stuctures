def quicksort(array,lo,hi):
    if lo < hi:
        mid = hoare_partition(array,lo,hi)
        quicksort(array,lo,mid-1)
        quicksort(array,mid+1,hi)
    return array

def swap(array,i,j):
    array[i], array[j] = array[j],array[i]

def hoare_partition(array,lo,hi):
    '''
    In Place

    Not Stable

    Example: 2a,2b,1
    Since 1 < 2, 2a and 1 are swapped

    Becomes

    1,2b,2a
    '''
    mid = (lo+hi)//2
    pivot = array[mid]
    swap(array,0,mid)
    L_bad = 1
    R_bad = hi
    while L_bad < R_bad:
        while array[L_bad] <= pivot and L_bad < R_bad:
            L_bad += 1
        while array[R_bad] > pivot and L_bad < R_bad:
            R_bad -= 1
        swap(array,L_bad,R_bad)
    swap(array,0,R_bad-1)
    return R_bad

array = [8,5,8,15,1,13,11,8,6]
lo = 0
hi = len(array)-1
print(quicksort(array,lo,hi))
