def sink_min(array,parent,heap_size):
    child = 2 * parent + 1
    while child <= heap_size:
        if child + 1 <= heap_size and array[child+1] < array[child]:
            child += 1
        if array[child] < array[parent]:
            swap(array,parent,child)
            parent = child
            child = 2 * parent + 1
        else:
            break

def insert_min(array,item):
    array.append(item)
    heap_size = len(array)-1
    rise_min(array,heap_size)

def rise_min(array,child):
    parent = (child-1)//2
    while parent >= 0:
        if array[child] < array[parent]:
            swap(array,parent,child)
            child = parent
            parent = (child-1)//2
        else:
            break

def sink_max(array,parent,heap_size):
    child = 2 * parent + 1
    while child <= heap_size:
        if child + 1 <= heap_size and array[child+1] > array[child]:
            child += 1
        if array[child] > array[parent]:
            swap(array,parent,child)
            parent = child
            child = 2 * parent + 1
        else:
            break

def insert_max(array,item):
    array.append(item)
    heap_size = len(array)-1
    rise_max(array,heap_size)

def rise_max(array,child):
    parent = (child-1)//2
    while parent >= 0:
        if array[child] > array[parent]:
            swap(array,parent,child)
            child = parent
            parent = (child-1)//2
        else:
            break

def swap(array,i,j):
    array[i],array[j] = array[j],array[i]

min_heap = []
max_heap = []
def online_median(array):
    global min_heap
    global max_heap

    if len(max_heap) == 0:
        if array[0] < array[1]:
            insert_max(max_heap,array[0])
            insert_min(min_heap,array[1])
        else:
            insert_max(max_heap,array[1])
            insert_min(min_heap,array[0])

    if len(max_heap) == 1:
        i = 2
    else:
        i = 0

    while i < len(array):
        if array[i] < max_heap[0]:
            insert_max(max_heap,array[i])
            sink_max(max_heap,0,len(max_heap)-1)
        else:
            insert_min(min_heap,array[i])
            sink_min(min_heap,0,len(min_heap)-1)
        i += 1

    while abs(len(max_heap)-len(min_heap)) > 1:
        if len(max_heap) > len(min_heap):
            tobereturned = max_heap.pop(0)
            insert_min(min_heap,tobereturned)
            sink_max(max_heap,0,len(max_heap)-1)
        else:
            tobereturned = min_heap.pop(0)
            insert_max(max_heap,tobereturned)
            sink_min(min_heap,0,len(min_heap)-1)
            
    if len(min_heap) == len(max_heap):
        median = (min_heap[0]+max_heap[0])//2
    elif len(min_heap) > len(max_heap):
        median = min_heap[0]
    else:
        median = max_heap[0]
   
    return median      
    
array = [21,43,27,2,9,41,3,8,11]
print(online_median(array))
print(min_heap)
print(max_heap)
more_elements = [5,10,14,20,20]
print(online_median(more_elements))
print(min_heap)
print(max_heap)
