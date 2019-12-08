class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        import copy
        n = len(mat)
        m = len(mat[0])
        l = m*n

        def flip(mtr, i, j):
            drc = [[1,0],[-1,0],[0,1],[0,-1],[0,0]]
            for dx, dy in drc:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if mtr[ny][nx] == 0:
                        mtr[ny][nx] = 1
                    else:
                        mtr[ny][nx] = 0
            # return mat

        def check(mat):
            for a in mat:
                for b in a:
                    if b == 1:
                        return False
            return True

        if check(mat):
            return 0
        
        M = copy.deepcopy(mat)
        cnt = []
        k = 1 << l
        for num in range(k):
            # print(bin(num))
            # cnt = 0
            M = copy.deepcopy(mat)
            # print('M:', M)
            for y in range(n):
                for x in range(m):
                    # print(M[y][x], num, y*m + x, (num >> (y*n + x)) & 1)
                    if (num >> (y*m + x)) & 1 == 1:
                        flip(M, x, y)
                        if (check(M)):
                            cnt.append(num)
                    # print(M,x,y)
            # print('final:',M)
        # print(cnt)   

        if cnt == []:
            return -1

        ans = []
        for i in cnt:
            n = 0
            for j in range(l):
                if (i >> j) & 1 == 1:
                    n += 1

            ans.append(n)
        
        # print(min(ans))
        return min(ans)


mat = [[0,0],[0,1]]
res = Solution().minFlips(mat)
print(res)

mat = [[0]]
res = Solution().minFlips(mat)
print(res)

mat = [[1,1,1],[1,0,1],[0,0,0]]
res = Solution().minFlips(mat)
print(res)

mat = [[1,0,0],[1,0,0]]
res = Solution().minFlips(mat)
print(res)

mat = [[0],[1],[1]]
res = Solution().minFlips(mat)
print(res)