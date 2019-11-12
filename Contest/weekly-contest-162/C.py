class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        self.flag = True
        
        def dfs(grid, row, col, x, y):
            if grid[x][y] == 1:
                return
            else:
                if x == 0 or x == row - 1 or y == 0 or y == col - 1:
                    self.flag = False

            grid[x][y] = 1

            if x != 0:
                dfs(grid, row, col, x - 1, y)
            if x != row - 1:
                dfs(grid, row, col, x + 1, y)
            if y != 0:
                dfs(grid, row, col, x, y - 1)
            if y != col - 1:
                dfs(grid, row, col, x, y + 1)

        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    dfs(grid, row, col, i, j)
                    if self.flag:
                        count += 1
                    self.flag = True
        return count

class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
   
        def dfs(grid, row, col, x, y):
            drct = [[0,1],[0,-1],[1,0],[-1,0]]
            flag = True
            grid[x][y] = 1
            
            if x == 0 or x == row - 1 or y == 0 or y == col - 1:
                flag = False    

            for dx, dy in drct:
                nx = x + dx; ny = y + dy
                if 0 <= nx <= row - 1 and 0 <= ny <= col - 1 and grid[nx][ny] != 1:
                    flag = flag & dfs(grid, row, col, nx, ny)
            return flag

        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    flag = dfs(grid, row, col, i, j)
                    if flag:
                        count += 1
        return count        

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
res = Solution().closedIsland(grid)
print(res)

grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
res = Solution().closedIsland(grid)
print(res)