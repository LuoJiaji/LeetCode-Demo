class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        n = len(grid)
        m = len(grid[0])
        self.ans = 0

        def dfs(x, y, cur):
            # print(x, y, cur, self.ans)
            tmp = grid[x][y]
            grid[x][y] = 0
            cur += tmp
            self.ans = max(self.ans, cur)
            # print(x, y, cur, self.ans)

            for dx,dy in d:
                tx = x + dx
                ty = y + dy
                if 0 <= tx and tx < n and 0 <= ty and ty < m and grid[tx][ty] > 0:
                    dfs(tx, ty, cur)
            grid[x][y] = tmp

            return self.ans
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    k = dfs(i,j,0)
        
        return self.ans

grid = [[0,6,0],[5,8,7],[0,9,0]]
res = Solution().getMaximumGold(grid)
print(res)

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
res = Solution().getMaximumGold(grid)
print(res)

a=  [1,2,3,4,5]
print(sum(a))