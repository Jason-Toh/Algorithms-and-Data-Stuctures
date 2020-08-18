import timeit
import random
#Quick Select is used to find the median as the pivot
#Quick Select is almost like Binary Search where we only need to go left OR go right, hence average case is O(n)
#Quick Sort go both left AND right, hence average case is O(nlogn)
def quickselect_recursive(array,lo,hi,k):
    if hi > lo:
        #randpivot = random.randrange(lo,hi+1)
        #swap(array,lo,randpivot)
        pivot = array[lo]
        mid = partition(array,lo,hi,pivot)
        #Checks if the kth position is less than mid, if yes, recurse left of the array
        if k < mid:
            return quickselect_recursive(array,lo,mid-1,k)
        #Checks if the kth position is more than mid, if yes, recurse right of the array
        elif k > mid:
            return quickselect_recursive(array,mid+1,hi,k)
        else:
            return array[k]
    else:
        return array[k]

def quickselect_iterative(array,lo,hi,k):
    while lo <= hi:
        randpivot = random.randrange(lo,hi+1)
        swap(array,lo,randpivot)
        pivot = array[lo]
        mid = partition(array,lo,hi,pivot)
        if k == mid:
            return array[k]
        elif k > mid:
            lo = mid + 1
        else:
            hi = mid - 1
    return array[k]

def partition(array,start,end,pivot):
    index = start
    for i in range(start+1,end+1):
        if array[i] < pivot:
            index += 1
            swap(array,index,i)

    swap(array,start,index)
    return index

def swap(array,i,j):
    array[i],array[j] = array[j],array[i]

recursion_count = [0]
def quicksort(array,lo,hi):
    global recursion_count
    recursion_count[0] += 1
    if lo < hi:
        k = (lo+hi)//2
        #quickselect_recursive(array,lo,hi,k)
        quickselect_iterative(array,lo,hi,k)
        quicksort(array,lo,k-1)
        quicksort(array,k+1,hi)
    return array

array = [11,3,10,16,5,4,1,20,6,18,7,8]
reverse_list = [10,9,8,7,6,5,4,3,2,1]#Worst Case when finding the median value
sorted_list = [1,2,3,4,5,6,7,8,9,10] #Best Case when finding the smallest element
lo = 0
hi = len(array)-1
k = 4 #kth smallest item, as in index k
k = (lo + hi)//2

start = timeit.default_timer()
#print(quickselect_recursive(array,lo,hi,k))
taken = timeit.default_timer() - start
print(taken)

start = timeit.default_timer()
print(quickselect_iterative(array,lo,hi,k))
taken = timeit.default_timer() - start
print(taken)

start = timeit.default_timer()
#print(quicksort(array,lo,hi))
taken = timeit.default_timer() - start
print(taken)

print(recursion_count)
