import timeit
recursion_count = [0]
def quicksort(array,lo,hi):
    global recursion_count
    recursion_count[0] += 1
    if lo < hi:
        mid = lomuto_partition(array,lo,hi)
        quicksort(array,lo,mid-1)
        quicksort(array,mid+1,hi)
    return array

def lomuto_partition(array,start,end):
    mid = (start + end)//2
    pivot = array[mid]
    array[start], array[mid] = array[mid], array[start]
    index = start
    for k in range(start+1,end+1):
        if array[k] < pivot:
            index += 1
            array[index],array[k] = array[k],array[index]

    array[start],array[index] = array[index],array[start]
    return index

            
array = [11,3,10,16,5,4,1,20,6,18,7,8]
print(len(array))
lo = 0
hi = len(array)-1
start = timeit.default_timer()
print(quicksort(array,lo,hi))
taken = timeit.default_timer() - start
print(taken)
print(recursion_count)
