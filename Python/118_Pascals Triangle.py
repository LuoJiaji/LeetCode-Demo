class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1],[1,1]]

        result = [[1],[1,1]]
        
        for i in range(numRows - 2):
            tmp  = [1]
            for j in range(len(result[-1]) - 1):
                tmp.append(result[-1][j] +result[-1][j+1])
            tmp.append(1)
            result.append(tmp)
            # print(tmp)
            # print(result)
        
        return result


result = Solution().generate(5)
print(result)

result = Solution().generate(6)
print(result)