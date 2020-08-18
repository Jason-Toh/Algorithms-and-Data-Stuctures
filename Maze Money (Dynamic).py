def maze_money(grid):
    memo = [0] * len(grid)
    for i in range(len(grid)):
        memo[i] = [0] * len(grid[i])

    for i in range(1,len(memo)):
        if grid[i][-1] == -1:
            break
        if grid[i][-1] > 0:
            memo[i][-1] += grid[i][-1]
        if memo[i-1][-1] > 0:
            memo[i][-1] += memo[i-1][-1]
            
    for j in range(len(grid[0])-2,-1,-1):
        if grid[0][j] == -1:
            break
        if grid[0][j] > 0:
            memo[0][j] += grid[0][j]
        if memo[0][j+1] > 0:
            memo[0][j] += memo[0][j+1]

    #print(*memo,sep="\n")

    for i in range(1,len(grid)):
        for j in range(len(grid[0])-2,-1,-1):
            
            if grid[i][j] == -1:
                continue

            if grid[i][j] > 0:
                k = grid[i][j]
            else:
                k = 0
                
            memo[i][j] = max(memo[i-1][j] + k,memo[i][j+1] + k)
            
    print(*memo,sep="\n")
            
    return memo[-1][0]
            
grid = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0,-1, 0, 0,-1, 0, 0, 0],
        [-1,-1, 1, 0, 0, 0,-1, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [ 0, 0, 0, 0,-1, 0, 0,-1, 0, 0],
        [ 0, 0,-1, 0, 0,-1, 0,-1, 0, 0],
        [ 0, 1,-1,-1, 0, 0, 0, 0, 0, 0],
        [ 0, 0,-1, 0, 0, 1, 0,-1,-1, 0],
        [ 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 1,-1,-1],
        [ 0, 0, 0, 0,-1, 0, 0, 0, 0, 0]]

print(maze_money(grid))
