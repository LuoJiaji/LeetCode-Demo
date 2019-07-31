class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        PathSum = [[0 for _ in grid[0]] for _ in grid]
        # print(PathSum)

        PathSum[0][0] = grid[0][0]
        for i in range(1,len(PathSum)):
            PathSum[i][0] = PathSum[i-1][0] + grid[i][0]
        # print(PathSum)
        
        for i in range(1,len(PathSum[0])):
            PathSum[0][i] = PathSum[0][i-1] + grid[0][i]
        # print(PathSum)

        for i in range(1,len(PathSum[0])):
            for j in range(1,len(PathSum)):
                PathSum[j][i] = min(PathSum[j][i-1], PathSum[j-1][i]) + grid[j][i]
        # print(PathSum)
        return PathSum[-1][-1]

data = [[1,3,1],
        [1,5,1],
        [4,2,1]]

result = Solution().minPathSum(data)
print(result)