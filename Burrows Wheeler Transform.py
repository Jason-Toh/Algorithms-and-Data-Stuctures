def merge_sort(alist,rank,k):
    temp = [None] * len(alist)
    lo = 0
    hi = len(alist)-1
    return merge_sort_aux(alist,lo,hi,temp,rank,k)

def merge_sort_aux(alist,lo,hi,temp,rank,k):
    if hi > lo:
        mid = (lo + hi)//2
        merge_sort_aux(alist,lo,mid,temp,rank,k)
        merge_sort_aux(alist,mid+1,hi,temp,rank,k)
        merge(alist,lo,mid,hi,temp,rank,k)

        #Assigning the temp list back into the original list
        for i in range(lo,hi+1):
            alist[i] = temp[i]
            
    return temp

#This merge is modified for prefix doubling
def merge(alist,lo,mid,hi,temp,rank,k):
    i = lo
    j = mid + 1

    #Left Half = array[lo..mid] (mid is inclusive)
    #Right Half = array[mid+1..hi] (hi is inclusive)

    index = lo
    while i < (mid+1) and j < (hi+1):
        if suffix_compare(rank,k,alist[i],alist[j]) == True:
            temp[index] = alist[i]
            i += 1
        else:
            temp[index] = alist[j]
            j += 1
        index += 1

    while i < (mid+1):
        temp[index] = alist[i]
        i += 1
        index += 1
        
    while j < (hi+1):
        temp[index] = alist[j]
        j += 1
        index += 1

def suffix_array_prefix_doubling(string):
    #Complexity for suffix_array with O(1) comparison
    #O(Nlog^2N) using prefix doubling O(1) comparison

    #SA is the suffix ID
    SA = [i for i in range(len(string))]
    #Rank contains the ord of all the suffixes
    rank = [ord(string[i])-96 for i in range(len(string))]

    #Perform Prefix Doubling here
    k = 1
    while k < len(string):
        SA = merge_sort(SA,rank,k)
        temp = [0] * len(string)
        for i in range(len(string)-1):
            #True is 1
            #False is 0
            temp[SA[i+1]] = temp[SA[i]] + suffix_compare(rank,k,SA[i],SA[i+1])

        #Swap rank with temp
        for i in range(len(rank)):
            rank[i] = temp[i]

        #Double k here
        k *= 2
    return SA

def suffix_compare(rank,k,i,j):
    #If the ranks are the the same, check if rank[i] < rank[i+1]
    if rank[i] != rank[j]:
        return rank[i] < rank[j]
    elif (i + k < len(rank)) and (j + k < len(rank)):
        return rank[i+k] < rank[j+k]
    else:
        return j < i

#print(suffix_array_prefix_doubling(string))
def suffix_array(string):
    return [suffix[1] for suffix in sorted((string[i:],i) for i in range(len(string)))]

def bwt(string):
    #SA = suffix_array(string)
    SA = suffix_array_prefix_doubling(string)
    #SA[i]-1 because of the cyclic property
    #Burrows Wheeler Transform is the last column of sorted strings
    #So the the previous of the first column is the last column hence SA[i]-1
    #Meaning first column -> last column
    return ''.join([string[SA[i]-1] for i in range(len(string))])

string = "banana$"
string2 = "mississippi$"
string3 = "acacia$"
string4 = "compression$"
string5 = "abbaab$"
print(bwt(string4))

#This is the fast and efficient way which is Last-First Mapping
#The entire complexity is O(n)
def inverse_bwt(bwt_string):
    '''
    Time Complexity: O(N^3) with radix sort
    Space Complexity: O(N^2) using k-mers (concatening the last and first, then first and second and so on and so forth)
    And then sort afterwards

    Time Complexity: O(N)
    Space Complexity: O(N) using LP Mapping
    '''
    size = 27
    order = [0] * len(bwt_string)
    count = [0] * size
    rank  = [1] * size

    #Pre computation takes O(n)
    #LP Mapping takes O(n)
    for i in range(len(bwt_string)):
        index = ord(bwt_string[i]) - 96
        #This is a one line if statement
        # if index > 0:
        #   index = index
        #else
        #   index = 0
        #index = index if index > 0 else 0

        #This is for if statement without else statement
        # if (condition is true) : value if condition if true
        #if index < 0: index = 0
        
        if index < 0:
            index = 0
            pos = i
        count[index] += 1
        order[i] = count[index]
        
    for i in range(1,len(count)):
        rank[i] = count[i-1] + rank[i-1]
        
    string = [None] * len(bwt_string)
    for i in range(len(string)-1,-1,-1):
        string[i] = bwt_string[pos]
        index = ord(bwt_string[pos])-96
        if index < 0: index = 0
        pos = rank[index] + order[pos] - 2
        
    return ''.join(string)

print(inverse_bwt("n$rsoocimpse"))
