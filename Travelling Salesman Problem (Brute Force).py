towns = ["Adelaide", "Brisbane", "Canberra", "Darwin", "Sydney"]
distance_matrix = [[   0, 2053, 1155, 3017, 1385],
                   [2053,    0, 1080, 3415,  939],
                   [1155, 1080,    0, 3940,  285],
                   [3017, 3415, 3940,    0, 3975],
                   [1385,  939,  285, 3975,    0]]

def permutations(a,b):#a is starting point,b is ending point, like how big you want your array,(1,6) will give [1,2,3,4,5]
    first=list(range(a,b))
    last=list(reversed(first))
    res=[first]
    while res[-1]!=last:
        res+=[lex_suc(res[-1])]
    return res

def lex_suc(perm):
    n=len(perm)
    res=perm[:]
    for i in range(n-2,-1,-1):
        if perm[i]<perm[i+1]:
            break
    for j in range(n-1,i,-1):
        if perm[j]>perm[i]:
            break
    res[i],res[j]=res[j],res[i]
    return res[:i+1] + list(reversed(res[i+1:]))

def brute_force_travelling_salesman_problem(distance,town):

    def cost(tour):
        res = 0
        for i in range(-1,len(tour)-1):
            res += distance[tour[i]][tour[i+1]]
        return res

    combinations = permutations(1,len(distance))

    opt = [0] + combinations[0]
    for tour in combinations:
        if cost([0] + tour) < cost(opt):
            opt = [0] + tour

    opt_town = []
    for i in opt:
        opt_town.append(town[i])
        
    return opt_town,opt

result = brute_force_travelling_salesman_problem(distance_matrix,towns)

total = 0
for i in range(1,len(result[1])):
    total += distance_matrix[result[1][i-1]][result[1][i]]
print(result,total)
