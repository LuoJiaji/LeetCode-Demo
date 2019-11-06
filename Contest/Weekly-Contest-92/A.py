class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])
        ans = []
        for i in range(n):
            tmp = []
            for j in range(m):
                tmp.append(A[j][i])
            ans.append(tmp)
        
        return ans

A = [[1,2,3],[4,5,6],[7,8,9]]
res = Solution().transpose(A)
print(res)

A = [[1,2,3],[4,5,6]]
res = Solution().transpose(A)
print(res)
