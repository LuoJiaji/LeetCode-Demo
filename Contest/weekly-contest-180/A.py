class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        c = []
        r = []

        for i in matrix:
            c.append(min(i))
        
        for i in range(len(matrix[0])):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[j][i])

            r.append(max(tmp))
        ans = []
        for i in c:
            if i in r:
                ans.append(i)

        return ans


matrix = [[3,7,8],[9,11,13],[15,16,17]]
res = Solution().luckyNumbers(matrix)
print(res)

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
res = Solution().luckyNumbers(matrix)
print(res)

matrix = [[7,8],[1,2]]
res = Solution().luckyNumbers(matrix)
print(res)
