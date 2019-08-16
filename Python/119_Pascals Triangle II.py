class Solution(object):
    def generate(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rowIndex += 1
        # if rowIndex == 0:
        #     return []
            
        if rowIndex == 0:
            return [1]

        if rowIndex == 2:
            return [1,1]

        result = [[1],[1,1]]
        
        for i in range(rowIndex - 2):
            tmp  = [1]
            for j in range(len(result[-1]) - 1):
                tmp.append(result[-1][j] +result[-1][j+1])
            tmp.append(1)
            result.append(tmp)
            # print(tmp)
            # print(result)
        
        return result[-1]


result = Solution().generate(3)
print(result)

result = Solution().generate(6)
print(result)