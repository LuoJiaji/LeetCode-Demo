class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        n = len(grid[0])
        m = len(grid)
        for i in range(n):
            for j in range(m):
                if grid[j][i] != 0:
                    for x in range(n):
                        if grid[j][x] == 1 and x != i:
                            grid[j][x] = 2
                    for y in range(m):
                        if grid[y][i] == 1 and y != j:
                            grid[y][i] = 2

        # print(grid)
        ans = 0 
        for i in grid:
            for j in i:
                if j == 2:
                    ans += 1

        return ans
        
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
res = Solution().countServers(grid)
print(res)