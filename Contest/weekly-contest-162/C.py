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


        


grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
res = Solution().closedIsland(grid)
print(res)

grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
res = Solution().closedIsland(grid)
print(res)