class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans = 0 
        m = len(matrix)
        n = len(matrix[0])

        for i in matrix:
            for j in i:
                if j == 1:
                    ans += 1

        i = 2
        # print(l)
        while i <= min(n,m):
            for y in range(0, m-i+1):
                for x in range(0, n-i+1):
                    flag = True
                    for k in range(i):
                        # print(matrix[y+k][x:x+i])
                        if 0 in matrix[y+k][x:x+i]:
                            flag = False
                            break
                    if flag:
                        ans += 1
                    # print(i, x, y, ans)
            i += 1
                    

        # print(ans)
        return ans


matrix =[[0,1,1,1],
         [1,1,1,1],
         [0,1,1,1]]
res = Solution().countSquares(matrix)
print(res)

matrix = [[1,0,1],
  [1,1,0],
  [1,1,0]]
res = Solution().countSquares(matrix)
print(res)