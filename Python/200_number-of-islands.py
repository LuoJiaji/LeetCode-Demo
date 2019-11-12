class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, row, col, i, j)
                    count += 1
        return count

    def dfs(self, grid, row, col, x, y):
        drct = [[0,1],[0,-1],[1,0],[-1,0]]
        grid[x][y] = '0'

        for dx, dy in drct:
                nx = x + dx; ny = y + dy
                if 0 <= nx <= row - 1 and 0 <= ny <= col - 1 and grid[nx][ny] != '0':
                    self.dfs(grid, row, col, nx, ny)


