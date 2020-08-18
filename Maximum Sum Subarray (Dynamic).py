def maximum_sum_subarray(array):

    memo = [0] * len(array)
    for i in range(len(array)):
        memo[i] = [0] * len(array)
        memo[i][i] = array[i]

    #print(*memo,sep="\n")

    #We are filling the matrix diagonally
    #This complexity is O(N*N)/2 which is still O(N^2)
    maximum_sum = 0
    for i in range(len(array)):
        for j in range(i,len(array)):
            memo[i][j] = memo[i][j-1] + memo[j][j]
            if memo[i][j] > maximum_sum:
                maximum_sum = memo[i][j]
                start = i
                end = j

    print(*memo,sep="\n")
    
    subarray = [None] * (end-start+1)
    index = len(subarray)-1
    while end > (start-1):
        subarray[index] = array[end]
        index -= 1
        end -= 1

    return maximum_sum,subarray

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#print(maximum_sum_subarray(array))

def maximum_sum_subarray_greedy(array):

    memo = [0] * (len(array)+1)
    index_list = [0] * (len(array)+1)

    #This approach here is greedy approach
    #The time complexity here is O(n)
    #memo[i] = sum(array[1..i]) inclusive of array[i]
    max_sum = 0
    for i in range(1,len(array)+1):
        #If the previous amount with the addition of the current amount than the current amount by itself, then add the current amount
        #Else, use the current amount instead
        sum1 = memo[i-1] + array[i-1]
        sum2 = array[i-1]
        if (sum1 > sum2):
            memo[i] = sum1
            #If the current subarray is less than optimal subarray with the one before
            index_list[i] = index_list[i-1]
        else:
            memo[i] = sum2
            index_list[i] = i
        if memo[i] > max_sum:
            max_sum = memo[i]
            get_max_index = i

    end = get_max_index
    start = index_list[end]
    subarray = [None] * (end - index_list[end] + 1)
    index = len(subarray)-1
    while end > (start-1):
        subarray[index] = array[end-1]
        index -= 1
        end -= 1
        
    return max_sum,subarray

print(maximum_sum_subarray_greedy(array))
