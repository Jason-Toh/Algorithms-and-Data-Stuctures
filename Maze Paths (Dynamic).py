def maze_paths(grid):
    
    memo = [0] * len(grid)
    for i in range(len(grid)):
        memo[i] = [0] * len(grid[i])
        
    memo[0][-1] = 1
    
    for i in range(1,len(memo)):
        if grid[i][-1] == 0:
            break
        else:
            memo[i][-1] = grid[i][-1]
            
    for j in range(len(grid[0])-2,-1,-1):
        if grid[0][j] == 0:
            break
        else:
            memo[0][j] = grid[0][j]

    #print(*memo,sep="\n")
    #print("\n")

    #memo[i][j] = memo[i][j+1] + memo[i-1][j]
    for i in range(1,len(grid)):
        for j in range(len(grid[i])-2,-1,-1):

            if grid[i][j] == 0:
                continue
            
            memo[i][j] = memo[i-1][j] + memo[i][j+1]
    
    print(*memo,sep="\n")
                
    return memo[-1][0]

grid = [[0,0,1,1,0,0,1],
        [0,0,1,1,1,1,1],
        [1,1,1,1,1,0,1],
        [1,1,1,1,0,1,1],
        [1,0,1,1,1,1,1],
        [1,0,0,1,1,0,0],
        [1,1,1,1,1,0,1]]

grid2 = [[1,1,1,1],
         [1,1,0,1],
         [1,1,1,0],
         [1,1,1,1]]
print(maze_paths(grid))
