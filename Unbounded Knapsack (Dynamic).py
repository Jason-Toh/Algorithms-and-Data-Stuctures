#Unbounded Knapsack
Item =    [1,2,3,4,5]
Weights = [4, 9, 10, 20, 2, 1]
Values =  [400, 1800, 3500, 4000, 1000, 200]
capacity = 20

#Bottom Up Approach
def Unbounded_Knapsack(Values,Weights,capacity):

    memo = [0] * (capacity+1)
    itemList = [None] * (capacity+1)

    for currentCapacity in range(1,capacity+1):
        maxValue = 0
        for i in range(1,len(Values)):
            if Weights[i] <= currentCapacity:
                balance = currentCapacity-Weights[i]
                currentValue = Values[i] + memo[balance]
                if currentValue > maxValue:
                    maxValue = currentValue
                    #Add the last recorded item into itemList
                    itemList[currentCapacity] = i
        memo[currentCapacity] = maxValue

    i = capacity
    item_chosen = []
    while i > 0:
        item_chosen.append(itemList[i])
        i -= Weights[itemList[i]]

    return memo[-1],item_chosen

#print(Unbounded_Knapsack(Values,Weights,capacity))

#Top Down Approach
def Top_Down_Knapsack(Values,Weights,capacity):
    memo = [-1] * (capacity+1)
    memo[0] = 0
    #memo = [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    itemList = [None] * (capacity+1)
    result = Top_Down_Knapsack_Aux(Values,Weights,capacity,memo,itemList)

    i = capacity
    item_chosen = []
    while i > 0:
        item_chosen.append(itemList[i])
        i -= Weights[itemList[i]]
        
    return result,item_chosen
    
def Top_Down_Knapsack_Aux(Values,Weights,capacity,memo,itemList):
    #Base Case when memo[capacity] != -1
    #This means when memo[capacity] = 0
    if memo[capacity] != -1:
        return memo[capacity]
    else:
        maxValue = 0
        #For each item
        for i in range(len(Values)):
            #Check the weight of the current item
            if Weights[i] <= capacity:
                #Keep breaking down the currentCapacity until it reaches the base case
                #At the same time, add the value of the current item
                currentValue = Values[i] + Top_Down_Knapsack_Aux(Values,Weights,capacity - Weights[i],memo,itemList)
                if currentValue > maxValue:
                    maxValue = currentValue
                    itemList[capacity] = i
        memo[capacity] = maxValue
        return memo[capacity]

#print(Top_Down_Knapsack(Values,Weights,capacity))
