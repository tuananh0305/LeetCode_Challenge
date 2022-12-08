'''
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is 1 or -1.
'''

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        pass_grid = [[False for i in range(n)] for j in range(m)]
        # print(pass_grid)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if j<n-1 and grid[i][j+1] == 1:
                        pass_grid[i][j] = True
                    else:
                        pass_grid[i][j] = False
                        
                elif grid[i][j] == -1:
                    if j>0 and grid[i][j-1] == -1:
                        pass_grid[i][j] = True
                    else:
                        pass_grid[i][j] = False
                        
        
        output = [-1 for i in range(n)]
        for k in range(n):
            j=k
            isPass=1
            for i in range(m):
                if pass_grid[i][j] == True:
                    if grid[i][j] == 1:
                        j+=1
                    elif grid[i][j] == -1:
                        j-=1
                    isPass=j
                else:
                    isPass=-1
                    break
            
            output[k] = isPass
        return output