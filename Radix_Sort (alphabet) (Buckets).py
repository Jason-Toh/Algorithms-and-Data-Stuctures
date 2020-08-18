import timeit
import random
import csv
def counting_sort_alpha(string_list,col,b):
    result = [None] * len(string_list)
    buckets = [[] for _ in range(b+1)]

    for string in string_list:
        if len(string) <= col:
            pos = 0
        else:
            pos = ord(string[col])-96
        buckets[pos].append(string)

    index = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            result[index] = buckets[i][j]
            index += 1

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
