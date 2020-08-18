#Sink has O(logk) operation
def sink(array,parent,heap_size):
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

def insert(array,item):
    array.append(item)
    heap_size = len(array)-1
    rise(array,heap_size)

def rise(array,child):
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

k_smallest_heap = []
def k_minimum_element_online(array,k):
    global k_smallest_heap
    i = 0
    #Operation is O(klogk)
    #Rise operation is used in insert and it is O(logk)
    #We repeat this operation for k times that is until a heap of size k is built

    #So k times calling rise operation (logk)
    while i < len(array) and len(k_smallest_heap) < k:
        insert(k_smallest_heap,array[i])
        i += 1

    #This operation here is O(Nlogk) since we are looping the rest of the array

    #There is a sink operation here which is O(logk)

    #We are calling sink operation N times

    #So O(Nlogk)

    #Note: k is the size of the heap
    while i < len(array):
        #We only need to compare the root node since it is max_heap which is O(1)
        if array[i] < k_smallest_heap[0]:
            k_smallest_heap[0] = array[i]
            sink(k_smallest_heap,0,len(k_smallest_heap)-1)
        i += 1
    return k_smallest_heap

k = 5
array = [3,11,21,43,27,2,9,41]
print(k_minimum_element_online(array,k))
more_elements = [6,40,15,23,11]
print(k_minimum_element_online(more_elements,k))
