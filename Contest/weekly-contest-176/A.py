class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        m = len(grid)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    cnt += n- j
                    break

        return cnt  


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
res = Solution().countNegatives(grid)
print(res)

grid = [[3,2],[1,0]]
res = Solution().countNegatives(grid)
print(res)

grid = [[1,-1],[-1,-1]]
res = Solution().countNegatives(grid)
print(res)

grid = [[-1]]
res = Solution().countNegatives(grid)
print(res)