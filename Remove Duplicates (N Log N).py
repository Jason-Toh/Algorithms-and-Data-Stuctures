#This algorithm should be in place and O(NlogN)
def remove_duplicates(array):
    i = 0
    j = 0
    while i < len(array)-1:
        if array[j] == array[i+1]:
            i += 1
        else:
            array[j+1],array[i+1] = array[i+1],array[j+1]
            j += 1
            i += 1
    return array[:j+1]
array = [1,1,2,2,3,4,4,4,7,8,9]# array must be sorted
string_list = ['aaa', 'aaa' ,'abc' ,'acb' ,'bac' ,'bca' ,'cab' ,'cab' ,'wxyz' ,'wxyz' ,'yzwx' ,'yzwx']
print(remove_duplicates(array))
print(remove_duplicates(string_list))

def remove_duplicates(array):
    array.sort() #In case if array not sorted
    j = 0
    for i in range(1,len(array)):
        if array[i] != array[i-1]:
            array[j+1] = array[i]
            j += 1
    return array[:j+1]

array = [1,1,2,2,3,4,4,4,7,8,9]# array must be sorted
string_list = ['aaa', 'aaa' ,'abc' ,'acb' ,'bac' ,'bca' ,'cab' ,'cab' ,'wxyz' ,'wxyz' ,'yzwx' ,'yzwx']
print(remove_duplicates(array))
print(remove_duplicates(string_list))
