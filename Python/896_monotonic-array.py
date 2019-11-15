class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag = A[-1] - A[0]

        if flag >= 0:
            for i in range(1, len(A)):
                if A[i] - A[i - 1] < 0:
                    return False
        else:
            for i in range(1, len(A)):
                if A[i] - A[i - 1] > 0:
                    return False
        return True

data = [1,2,2,3]
res = Solution().isMonotonic(data)
print(res)

data = [6,5,4,4]
res = Solution().isMonotonic(data)
print(res)

data = [1,3,2]
res = Solution().isMonotonic(data)
print(res)

data = [1,1,1]
res = Solution().isMonotonic(data)
print(res)