#Longest Increasing Subsequence
#The Longest Increasing Subsequence (LIS) problem is to find the
#length of the longest subsequence of a given sequence such that all elements of the subsequence are
#sorted in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

def LIS (num_list):

    #Time Complexity is O(N^2)
    #Auxilliary Space is O(2N + m + 1) = O(N + m) = O(N) since m is a subset of N which is smaller or equal to N
    #Where N is for memo of size N + 1
    #Where N is for saved_index of size N + 1
    #Where m is for sequence where m is the maximum sequence length

    #Initilize a memo with all [1]
    memo = [1] * (len(num_list)+1)
    #memo[0] is the base case
    memo[0] = 0

    maxSequence = 0
    #Saved index stores the second last index before i
    saved_index = [0] * (len(num_list)+1)
    #memo[i] = num_list[1..i] inclusive num_list[i]
    for i in range(2,len(num_list)+1):
        # 0 <= j < i-1
        currentMaxSequence = 0
        # j is the number all before i - 1
        for j in range(0,i-1):
            if num_list[j] < num_list[i-1]:
                #memo[j+1] because the first element is empty
                currentSequence = memo[j+1]
                #Check if the current sequence is more than current max Sequence
                if currentSequence > currentMaxSequence:
                    currentMaxSequence = currentSequence
                    saved_index[i] = j + 1
                    #If the current maximum sequence for that number is overall maximum sequence for the whole list
                    if (currentMaxSequence + 1) > maxSequence:
                        maxSequence = (currentMaxSequence + 1)
                        getMaxIndex = i
        memo[i] = currentMaxSequence + 1

    sequence = [None] * maxSequence
    index = len(sequence)-1
    i = getMaxIndex
    while i > 0:
        #Add the last known item to the list
        sequence[index] = num_list[i-1]
        #Saved index contains the last known index of an item before adding the current item
        i = saved_index[i]
        index -= 1

    return maxSequence,sequence
    
#num_list = [3,4,-1,0,6,2,3]
#num_list2 = [3,7,5,6,1,2,3,4,5,9,21,11,3,4]
num_list3 = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(LIS(num_list3))
