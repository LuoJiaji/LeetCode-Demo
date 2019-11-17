class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for _ in range(k):
            for i in range(len(grid)):
                grid[i] = [grid[i][-1]] + grid[i][0:-1]
                # print(grid[i])
            
            curr = []
            for i in range(len(grid)):
                curr.append(grid[i][0])
            curr = [curr[-1]] + curr[0:-1]
            
            for i in range(len(grid)):
                grid[i][0] = curr[i]

        # print(grid)
        return grid
        
grid = [[1,2,3],[4,5,6],[7,8,9]]; k = 1
res = Solution().shiftGrid(grid, k)
print(res)

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]; k = 4
res = Solution().shiftGrid(grid, k)
print(res)