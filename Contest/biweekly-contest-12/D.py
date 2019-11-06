class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        f = [[127 for _ in range(105)]  for _ in range(105)]
        # f[0][0] = 1
        # print(len(f), len(f[0]))
        # print(f)
        n = len(arr)
        for i in range(n):
            f[i][i] = 1
        # print('l', 'i', 'j', 'k')
        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                for k in range(i, j):
                    print(l, i, j, k)
                    f[i][j] = min(f[i][j], f[i][k] + f[k+1][j])
                    if arr[i] == arr[j]:
                        if l == 1:
                            f[i][j] = 1
                        else:
                            f[i][j] = min(f[i][j], f[i+1][j-1])
        return f[0][n-1]

arr = [1,2]
res = Solution().minimumMoves(arr)
print(res)

arr = [1,3,4,1,5]
res = Solution().minimumMoves(arr)
print(res)

arr = [4,1,14,16,15,18,19,17,10,8,10,4,19,17,14,17,2,1,14,11]
res = Solution().minimumMoves(arr)
print(res)

arr = [10,8,15,2,4,8,8,7,10,10,19,11,2,7,15,7,20,20,1,5,11,4,7,19,2,12,19,14,6,18,6,18,18,20,7,17,12,18,9,12,1,18,12,5,17,19,3,12,2,3,18,17,9,3,14,16,2,12,9,19,1,16,3,2,17,17,12,15,10,3,20,15,6,10,2,1,19,2,7,17,1,4,2,10,20,18,14,12,12,16,2,3,14,10,5,2,18,13,13,16]
res = Solution().minimumMoves(arr)
print(res)
