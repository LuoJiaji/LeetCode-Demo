class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        dp = [[0]*16 for _ in range(16)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = 1 if i == j else i*j
                for p in range(1, i+1):
                    dp[i][j]=min(dp[i][j], dp[p][j] + dp[i-p][j])
                for p in range(1, j+1):
                    dp[i][j]=min(dp[i][j], dp[i][p] + dp[i][j-p])
                for x in range(2, i+1):
                    for y in range(2, j+1):
                        dp[i][j]=min(dp[i][j], dp[x-1][y] + dp[x][j-y] + dp[i-x+1][y-1] + dp[i-x][j-y+1] + 1)
        # print(dp)
        return dp[n][m]

res = Solution().tilingRectangle(2, 3)
print(res)

res = Solution().tilingRectangle(5, 8)
print(res)
