#Minimum Edit Distance (Dynamic)

def Minimum_Edit_Distance(string1,string2):

    #for x is the inner for loop
    #for y is the outer for loop

    #memo = [[(x+y)*(not(y and 1) or not(x and 1)) for x in range(len(string1)+1)]for y in range(len(string2)+1)]

    memo = [0] * (len(string1)+1)
    count = 0
    for i in range(len(string1)+1):
        memo[i] = [0] * (len(string2)+1)
        memo[i][0] = count
        count += 1
    memo[0] = list(range(len(string2)+1))

    #print(*memo,sep="\n")
    
    #Going diagonal is replace
    #Going left is insert
    #Going up is delete

    # replace | delete
    #---------|--------
    # insert  | you are here
    
##    for x in range(len(string2)+1):
##        print ("x = ", end='')
##        print (x, end=' is ')
##        print (not(x and 1))
##
##    for y in range(len(string1)+1):
##        print ("y = ", end='')
##        print (y, end=' is ')
##        print (not(y and 1))

##    memo[0] = [x for x in range(len(string1)+1)]
##    x = 0
##    for line in memo:
##        line[0] = x
##        x += 1

    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            #If the last characters of the both strings are the same,we don't need to make any edits, just take the previous operation
            if string1[i-1] == string2[j-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                #Choosing the minimum edit distance between replace,insert and delete
                #min(replace,delete,insert)
                memo[i][j] = min(memo[i-1][j-1],memo[i-1][j],memo[i][j-1]) + 1

    #print(*memo,sep="\n")

    edit_list = []
    i = len(string1)
    j = len(string2)
    print("Convert '" + string1 + "' To '" + string2 + "'")
    while i > 0 and j > 0:
        #This part is for replacing
        if string1[i-1] != string2[j-1]:
            if (memo[i-1][j-1] + 1) == memo[i][j]:
                edit_list.append(string1[i-1] + " replace with " + string2[j-1] + " at position " + str(i))
                i -= 1
                j -= 1
            #This is for deleting
            elif (memo[i-1][j] + 1) == memo[i][j]:
                edit_list.append("delete " + string1[i-1] + " at position " + str(i))
                i -= 1
            #This is for inserting
            elif (memo[i][j-1] + 1) == memo[i][j]:
                edit_list.append("insert " + string2[j-1] + " at position " + str(j))
                j -= 1
        else:
            i -= 1
            j -= 1

    return memo[-1][-1], edit_list

string1 = "azce"
string2 = "abcdef"
#string1 = "benyam"
#string2 = "ephrem"
#string1 = "sings"
#string2 = "shine"
result = Minimum_Edit_Distance(string1,string2)
print(result)
