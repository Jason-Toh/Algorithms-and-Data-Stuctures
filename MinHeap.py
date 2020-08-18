class MinHeap:
    def __init__(self, size):
        self.array = [None] * size
        self.counter = 0
        self.index_array = [None] * size

    def is_empty(self):
        return self.counter == 0

    def is_full(self):
        return self.counter == len(self.array)

    def size(self):
        return self.counter

    def __str__(self):
        temp = ""
        for i in range(self.counter):
            comma = ""
            if i != (self.counter-1):
                comma = ", "
            temp = temp + str(self.array[i]) + comma
        return temp
    
    def add(self, key, data = None):
        if self.counter < len(self.array):
            self.array[self.counter] = (key, data)
            self.index_array[key.vertex_id] = self.counter
        else:
            raise Exception("Heap is full")
        self.rise(self.counter)
        self.counter += 1

    def rise(self, child):
        parent = (child-1)//2
        while parent >= 0 and self.array[child][1] < self.array[parent][1]:
            self.swap(child,parent)
            child = parent
            parent = (child-1)//2

    def get_min(self):
        tobereturned = self.array[0]
        self.swap(0,self.counter-1)
        self.counter -= 1
        self.sink(0)
        return tobereturned

    def sink(self, parent):
        while 2 * parent + 1 < self.counter:
            child = self.smallest_child(parent)
            if self.array[parent][1] < self.array[child][1]:
                break
            self.swap(parent, child)
            parent = child

    def smallest_child(self, parent):
        if 2*parent+1 == (self.counter-1) or self.array[2*parent+1][1] < self.array[2*parent+2][1]:
            return 2*parent+1
        else:
            return 2*parent+2

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
        i = self.array[i][0].vertex_id
        j = self.array[j][0].vertex_id
        self.index_array[i],self.index_array[j] = self.index_array[j],self.index_array[i]

    #Time complexity is O(logV)
    #Accessing the index_array is O(1)
    #Performing rise operation is O(logV)
    def update(self,key,value):
        index = self.index_array[key.vertex_id]
        new_tuple = (key,value)
        self.array[index] = new_tuple
        self.rise(index)
        
def heapsort(alist):
    result = []
    minheap = MinHeap(len(alist))
    
    for item in alist:
        minheap.add(item)

    while not minheap.is_empty():
        result.append(minheap.get_min()[0])

    return result