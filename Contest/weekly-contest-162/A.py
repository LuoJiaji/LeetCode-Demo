class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        # print(matrix)

        for r,c in indices:
            for i in range(m):
                matrix[r][i] += 1
            for i in range(n):
                matrix[i][c] += 1
            # print(matrix)
        cnt = 0
        for vec in matrix:
            for i in vec:
                if i % 2 == 1:
                    cnt += 1
        return cnt 
 
n = 2
m = 3
indices = [[0,1],[1,1]]
res = Solution().oddCells(n,m,indices)
print(res)

n = 2
m = 2
indices = [[1,1],[0,0]]
res = Solution().oddCells(n,m,indices)
print(res)