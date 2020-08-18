towns = ["Adelaide", "Brisbane", "Canberra", "Darwin", "Sydney"]
distance_matrix = [[   0, 2053, 1155, 3017, 1385],
                   [2053,    0, 1080, 3415,  939],
                   [1155, 1080,    0, 3940,  285],
                   [3017, 3415, 3940,    0, 3975],
                   [1385,  939,  285, 3975,    0]]

def totalRoute(partialSolution,distances):
    total = 0

    if partialSolution == []:
        return float("inf")
    
    for i in range(1,len(partialSolution)):
        total += distances[partialSolution[i-1]][partialSolution[i]]

    return total

def getCities(partialSolution,distances):
    possible = []
    
    for i in range(len(distances)):
        if i not in partialSolution:
            possible.append(i)

    return possible

def backtrack_travelling_salesman_problem(partialSolution,currentSolution,distances):

    possibleCities = getCities(partialSolution,distances)

    if possibleCities == []:
        temp = []
        routeLength = totalRoute(partialSolution,distances)
        currentMin = totalRoute(currentSolution,distances)
        if routeLength < currentMin:
            for i in range(len(partialSolution)):
                temp.append(partialSolution[i])
            currentSolution = temp
    else:
        for city in possibleCities:
            partialSolution.append(city)
            currentSolution = backtrack_travelling_salesman_problem(partialSolution,currentSolution,distances)
            partialSolution.pop()

    return currentSolution

solution = []
result = backtrack_travelling_salesman_problem([],solution,distance_matrix)
print([towns[i] for i in result])
print(result,totalRoute(result,distance_matrix))
