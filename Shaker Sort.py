def shaker_sort(a_list):
    '''
    This function sorts the list given from left to right and right to left
    :param a_list: a list
    :return: a sorted list
    :raises: None
    :precondition: the list must be integers
    :complexity: best case O(n),worst case O(n^2),where n is the a_list
    '''
    n = len(a_list)
    left = 0
    right = n - 1
    swapped = True
    while swapped:
        
        swapped = False

        #Looping from left to right
        for i in range(left,right):
            if a_list[i] > a_list[i+1]: #if current item is larger than the item on the right
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
                swapped = True
        right = right - 1

        if not swapped:
            break

        #Looping from right to left
        for i in range(right,left,-1):
            if a_list[i] < a_list[i-1]: #if item on the left is larger than the current item
                a_list[i],a_list[i-1] = a_list[i-1],a_list[i]
                swapped = True
        left = left + 1
        
    return a_list

alist = [54,26,93,17,77,31,44,55,20]
print(shaker_sort(alist))
