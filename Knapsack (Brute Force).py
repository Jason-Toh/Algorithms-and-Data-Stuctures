values = [400, 1800, 3500, 4000, 1000, 200]
weights = [4, 9, 10, 20, 2, 1]
capacity = 20

def bitlists(n):
    first=n*[0]
    last=n*[1]
    res=[first]
    while res[-1]!=last:
        res+=[lex_suc(res[-1])]
    return res

def lex_suc(bitlist):
    res=bitlist[:]
    i=len(res)-1
    while res[i]==1:
        res[i]=0
        i-=1
    res[i]=1
    return res

def brute_force_knapsack(values,weights,capacity):

    def is_feasible(subset):
        weight = 0
        for i in range(len(subset)):
            if subset[i] == 1:
                weight += weights[i]
        return weight <= capacity

    def value(subset):
        total = 0
        for i in range(len(subset)):
            if subset[i] == 1:
                total += values[i]
        return total

    def mass(subset):
        total = 0
        for i in range(len(subset)):
            if total <= capacity:
                if subset[i] == 1:
                    total += weights[i]
        return total
            
    combinations = bitlists(len(values))
    feasible = []
    for sol in combinations:
        if is_feasible(sol):
            feasible += [sol]

    opt = feasible[0]
    for sol in feasible:
        if value(sol) > value(opt):
            opt = sol

    sel = []
    for i in range(len(opt)):
        if opt[i] == 1:
            sel.append(i)

    return sel,value(opt),mass(opt)

print(brute_force_knapsack(values,weights,capacity))
