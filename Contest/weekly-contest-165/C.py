# class Solution(object):
#     def countSquares(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#         ans = 0 
#         m = len(matrix)
#         n = len(matrix[0])

#         for i in matrix:
#             for j in i:
#                 if j == 1:
#                     ans += 1

#         i = 2
#         # print(l)
#         while i <= min(n,m):
#             for y in range(0, m-i+1):
#                 for x in range(0, n-i+1):
#                     flag = True
#                     for k in range(i):
#                         # print(matrix[y+k][x:x+i])
#                         if 0 in matrix[y+k][x:x+i]:
#                             flag = False
#                             break
#                     if flag:
#                         ans += 1
#                     # print(i, x, y, ans)
#             i += 1
                    

#         # print(ans)
#         return ans


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        cnt = [[0 for _ in range(m+1)] for _ in range(n+1)]

        def get(x0, y0, l):
            x1 = x0 + l - 1
            y1 = y0 + l - 1
            return cnt[x1][y1] - cnt[x1][y0-1] - cnt[x0-1][y1] + cnt[x0-1][y0-1]
        
        for i in range(n):
            for j in range(m):
                cnt[i+1][j+1] = matrix[i][j]

        for i in range(1, n+1):
            for j in range(1, m+1):
                cnt[i][j] += cnt[i][j-1]

        for i in range(1, n+1):
            for j in range(1, m+1):
                cnt[i][j] += cnt[i-1][j]

        print(cnt)
        ans = 0
        for i in range(1,n+1):
            for j in range(1, m+1):
                for l in range(1, min(n-i+2, m-j+2)):
                    if get(i,j,l) == l*l:
                        ans += 1
                    else:
                        break
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



