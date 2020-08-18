values = [400, 1800, 3500, 4000, 1000, 200]
weights = [4, 9, 10, 20, 2, 1]
capacity = 20

def getTotal(partialSolution,aList):
    total = 0
    for items in partialSolution:
        total += aList[items]
    return total

def getItems(partialSolution,Weights,Capacity):
    possible = []
    currentWeight = getTotal(partialSolution,Weights)

    for i in range(len(Weights)):
        if len(partialSolution) == 0 or i > partialSolution[-1]:
            if currentWeight + Weights[i] <= capacity:
                possible.append(i)
                
    return possible

def backtrack_knapsack(partialSolution,currentSolution,Weights,Values,Capacity):

    possibleItems = getItems(partialSolution,Weights,Capacity)

    if len(possibleItems) == 0:
        myValue = getTotal(partialSolution,Values)
        print(partialSolution,myValue)

        currentMax = getTotal(currentSolution,Values)

        if myValue > currentMax:
            currentSolution.clear()
            currentSolution += partialSolution

    else:
        for item in possibleItems:
            partialSolution.append(item)
            currentSolution = backtrack_knapsack(partialSolution,currentSolution,Weights,Values,Capacity)
            partialSolution.pop()

    return currentSolution

solution = []
result = backtrack_knapsack([],solution,weights,values,capacity)
value = 0
for item in result:
    value += values[item]
print(result,value)


