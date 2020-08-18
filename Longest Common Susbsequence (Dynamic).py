#Longest Common Subsequence (Dynamic)

def LCS(string1,string2):

    #Time complexity of this algorithm is O(NM)

    #string1 = s1[1...N] N is the length of string1
    #string2 = s2[1...M] M is the length os string2

    #for x is the inner for loop
    #for y is the outer for loop

    #memo = [[0 for x in range(len(string1)+1)]for y in range(len(string2)+1)]
    memo = [0] * (len(string1)+1)
    for i in range(len(string1)+1):
        memo[i] = [0] * (len(string2)+1)

    #Use this to check the memo size
    #print(*memo,sep="\n")

    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            #If the last character of string 1 and string 2 are the same, we'll take the previous substring and add 1 
            if string1[i-1] == string2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                #We choose whether to include the last character of string1 or not
                #max(exclude,include)
                memo[i][j] = max(memo[i-1][j],memo[i][j-1])

    print(*memo,sep="\n")
                
    letter_chosen = [None] * memo[-1][-1] #initiliaze the length of the solution with the optimal length
    i = len(string1)
    j = len(string2)
    index = len(letter_chosen)-1
    while i > -1 and j > -1:
        if memo[i][j] != memo[i-1][j] and memo[i][j] != memo[i][j-1]:
            letter_chosen[index] = string1[i-1]
            j -= 1
            i -= 1
            index -= 1
        elif memo[i][j] == memo[i-1][j]:
            i -= 1
        elif memo[i][j] == memo[i][j-1]:
            j -= 1

    return memo[-1][-1],letter_chosen

##string1 = "abcdaf"
##string2 = "acbcf"
# string1 = "aabcd"
# string2 = "abxc"
string1 = "12341"
string2 = "341213"
result = LCS(string1,string2)
print(result)
