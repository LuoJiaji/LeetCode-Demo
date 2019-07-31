class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        n = 0
        for i in range(len(matrix)):
            if target >= matrix[i][0]:
                n = i
        for i in range(len(matrix[0])):
            if target == matrix[n][i]:
                # print(n,i)
                return True
        return False


data = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
result = Solution().searchMatrix(data, target)
print(result)

target = 13
result = Solution().searchMatrix(data, target)
print(result)


data = [[1],[3]]
target = 3
result = Solution().searchMatrix(data, target)
print(result)