class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        result = [[0 for i in range(n)] for j in range(n)]
        # print(result)

        counter = 1
        for i in range(int(n/2)):
            for j in range(i,n-i):
                result[i][j] = counter
                counter += 1
            # print(result)

            for j in range(i+1, n-i-1):
                result[j][n-i-1] = counter
                counter += 1

            for j in range(i,n-i):
                result[n-i-1][n-j-1] = counter
                counter += 1

            for j in range(i+1, n-i-1):
                result[n-j-1][i] = counter
                counter += 1
            # print(result)

        if (n%2 == 1):
            result[int(n/2)][int(n/2)] = counter
            # print(result)
        return result


result = Solution().generateMatrix(3)
print(result)
result = Solution().generateMatrix(2)
print(result)
result = Solution().generateMatrix(1)
print(result)