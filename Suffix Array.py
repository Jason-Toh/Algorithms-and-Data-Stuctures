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
##        if rank[alist[i]] < rank[alist[j]]:
##            temp[index] = alist[i]
##            i += 1
##        elif rank[alist[i]] == rank[alist[j]]:
##            if (alist[i] + k < len(rank) and alist[j] + k < len(rank)):
##                if rank[alist[i] + k] <= rank[alist[j] + k]:
##                    temp[index] = alist[i]
##                    i += 1
##                else:
##                    temp[index] = alist[j]
##                    j += 1
##            else:
##                temp[index] = alist[i]
##                i += 1
##        else:
##            temp[index] = alist[j]
##            j += 1
##        index += 1
    #Checking if any element was left   
    while i < (mid+1):
        temp[index] = alist[i]
        i += 1
        index += 1
        
    while j < (hi+1):
        temp[index] = alist[j]
        j += 1
        index += 1

def generate_suffixes(string):
    #Complexity is O(N^2)
    #There are N suffixes
    #Every suffix is as long as 1 all the way up to N
    #So total complexity is O(N^2)
    suffix_list = [None] * len(string)
    for i in range(len(string)):
        suffix_list[i] = (string[i:],i)
    return suffix_list
'''
Usage: Can be used to search for substring
    With Binary Search
    Complexity is O(MlogN)
    M is the length of the pattern

    Can be used to find longest repeated substring
'''
#Naive_implementation
def suffix_array_naive(string):
    suffix_list = generate_suffixes(string)
    #Merge_sort for strings is (kNlogN)
    #Merge_sort for suffixes is (N^2logN)
    #Merge_sort is NlogN
    #Comparison_cost for string is k
    #But since this is sorting suffixes
    #Longest suffix is N
    #So (N^2)logN
    #Space Complexity is O(N^2) because we need all the suffixes

    #This is supposed to be merge sort
    #But since merge sort is modified, we'll just sort() for illustration
    suffix_list.sort() 
    index_list = [None] * len(string)
    for i in range(len(suffix_list)):
        index_list[i] = suffix_list[i][1]
    return index_list

string = "mississippi$"
string2 = "banana$"
string3 = "jararaka$"
print(suffix_array_naive(string3))

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
        #If yes, return true which is 1
        #else, return false which is 0
        return rank[i] < rank[j]
    #If there are with range of rank
    #Check for the rank values for it
    elif (i + k < len(rank)) and (j + k < len(rank)):
        return rank[i+k] < rank[j+k]

    #Actually, this whole else statement is totally redundant
    #Cause the last character is the $ sign which means
    #The rank of it will go to the first if statement which is rank[i] != rank[j]
    else:
        #If (i + k > len(rank)) or (j + k > len(rank))
        #Then check which of the suffix ID is bigger
        #Because suffix ID = 11 is i$
        #Suffix ID = 8 is ippi$
        #So i$ is smaller than ippi$

        #so j = 8 and i = 11
        #Since 8 is smaller than 11
        #Than temp[8] = temp[11] + True(since j(8) < i(11))
        #return 1
        return j < i #To be honest, this will always return True

print(suffix_array_prefix_doubling(string3))
'''
In computer science, pattern matching is the act of checking a given sequence of tokens for the presence of the 
constituents of some pattern.
In contrast to pattern recognition, the match usually has to be exact: "either it will or will not be a match."
'''
