class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        l = len(colsum)
        matrix = [[0 for _ in range(l)] for _ in range(2)]
        # print(matrix)
        cnt = 0
        cnt_12 = 0
        sum_0 = 0
        sum_1 = 0
        for i in range(l):
            if colsum[i] == 2:
                cnt_12 += 1
        for i in range(l):
            if colsum[i] == 0:
                continue
            elif colsum[i] == 2:
                matrix[0][i] = 1
                matrix[1][i] = 1
                sum_0 += 1
                sum_1 += 1
            else:
                if cnt < upper-cnt_12:
                    matrix[0][i] = 1
                    cnt += 1
                    sum_0 += 1
                else:
                    matrix[1][i] = 1
                    sum_1 += 1
        if sum_0 != upper or sum_1 != lower:
            return []
        return matrix

upper = 2
lower = 1
colsum = [1,1,1]
res = Solution().reconstructMatrix(upper, lower, colsum)
print(res)

upper = 2
lower = 3
colsum = [2,2,1,1]
res = Solution().reconstructMatrix(upper, lower, colsum)
print(res)

upper = 5
lower = 5
colsum = [2,1,2,0,1,0,1,2,0,1]
res = Solution().reconstructMatrix(upper, lower, colsum)
print(res)


upper = 4
lower = 2
colsum = [1,2,1,2,0]
res = Solution().reconstructMatrix(upper, lower, colsum)
print(res)

upper = 9
lower = 2
colsum = [0,1,2,0,0,0,0,0,2,1,2,1,2]
res = Solution().reconstructMatrix(upper, lower, colsum)
print(res)

