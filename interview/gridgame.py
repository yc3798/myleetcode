#
# Complete the 'gridGame' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY grid
#  2. INTEGER k
#  3. STRING_ARRAY rules
#

def gridGame(grid, k, rules):
    # Write your code here

    # extract rules
    n = len(rules)
    alive_rules = [i for i in range(n) if rules[i] == 'alive']
    print(alive_rules)
    new_grid = grid
    ini_k = k
    while k != 0:
        print("--- ROUND #", ini_k+1 - k)
        new_grid = helper(new_grid, alive_rules)
        printGrid(new_grid)
        k -= 1

    return new_grid


def helper(grid, rules):
    """
    return new grid
    """
    row = len(grid)
    col = len(grid[0])
    new_grid = grid

    for i in range(row):
        for j in range(col):
            count = 0
            neigb = getNeighbors(row,col,i,j)

            for (m,n) in neigb:
                count += grid[m][n] #alive

            if count in rules:
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = 0
    print(grid, new_grid, rules)

    return new_grid

def getNeighbors(row,col,i,j):
    """
    Generate valid neighbours list
    """
    neigb = []

    for m in [i-1,i,i+1]:
        for n in [j-1,j,j+1]:
            if (not (m == i and j == n)) and row > m >= 0 and col > n >= 0: #within bound
                neigb.append((m,n))

    return neigb


def printGrid(grid):
    print("NEW GRID\n")
    for row in grid:
        print(row)


if __name__ == '__main__':
    printGrid([[0,1,1,0],[1,1,0,0]])

    # gridGame(None, None, ['dead', 'alive', 'dead', 'dead', 'dead', 'dead', 'dead', 'dead', 'dead'])
    ans = gridGame([[0,1,1,0],[1,1,0,0]], 2, ['dead', 'dead', 'dead', 'alive', 'dead', 'alive'])
    print(ans)
