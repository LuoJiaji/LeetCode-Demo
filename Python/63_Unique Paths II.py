class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        ways = [0] * n

        state = 1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            else:
                ways[i] = 1
        print(ways)

        for i in range(1, m):
            for j in range(0, n):
                # print(i,j,obstacleGrid[j][i])
                if j == 0:
                    if obstacleGrid[j][i] == 1:
                        ways[j] = 0
                    # else:
                    #     ways[j] =  ways[j]
                else:
                    if obstacleGrid[j][i] == 1:
                        ways[j] = 0
                    else:
                        ways[j] += ways[j - 1]
            print(ways)
        return ways[n - 1]


data = [[0,0,0],
        [0,1,0],
        [0,0,0]]
result = Solution().uniquePathsWithObstacles(data)

data = [[0,0],[1,1],[0,0]]
result = Solution().uniquePathsWithObstacles(data)

data = [[0,1]]
result = Solution().uniquePathsWithObstacles(data)

data = [[1,0]]
result = Solution().uniquePathsWithObstacles(data)