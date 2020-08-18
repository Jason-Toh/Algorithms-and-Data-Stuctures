def counting_sort_alpha(string_list,col,b):
    count_list = (b+1)*[0]
    position = (b+1)*[0]
    result = [None] * len(string_list)

    for string in string_list:
        if len(string) <= col:
            pos = 0
        else:
            pos = ord(string[col])-96
        count_list[pos] += 1

    position[0] += count_list[0]
    for i in range(1,len(position)):
        position[i] = position[i-1] + count_list[i]
    
    for i in range(len(string_list)-1,-1,-1):
        if len(string_list[i]) <= col:
            pos = 0
        else:
            pos = ord(string_list[i][col])-96
        result[position[pos]-1] = string_list[i]
        position[pos] -= 1

    return result

def radix_sort_alpha(string_list,b):

    if len(string_list) == 0:
        return string_list

    max_length = len(string_list[0])
    result = []
    for string in string_list:
        result.append(string)
        if len(string) > max_length:
            max_length = len(string)

    for col in range(max_length-1,-1,-1):
        result = counting_sort_alpha(result,col,b)
        
    return result

string_list = ["aaa","abc","cab","acb","wxyz","yzwx"]
#print(radix_sort_alpha(string_list,26))

string_list = ["fc","osg","rky","csu","lk","abcd"]
#print(radix_sort_alpha(string_list,26))

string_list = ['aaa','abc','','cab']
print(radix_sort_alpha(string_list,26))
