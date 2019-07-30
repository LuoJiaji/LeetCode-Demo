class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        result = []
        m = len(matrix)
        n = len(matrix[0])
        # print(m,n)
        it = min(m,n)
        # print(it)
        up , down, left, right = 0, m, 0, n
        result = []
        
        if m == 1:
            for i in range(n):
                result.append(matrix[0][i])
            return result
        elif n == 1:
            for i in range(m):
                result.append(matrix[i][0])
            return result

        for i in range(int(it/2)):
            for j in range(left, right):
                # print(matrix[i][j])
                result.append(matrix[i][j])
            for j in range(up+1, down-1):
                # print(matrix[j][n-i-1])
                result.append(matrix[j][n-i-1])
            for j in range(left, right):
                # print(matrix[m-i-1][n-j-1])
                result.append(matrix[m-i-1][n-j-1])
            for j in range(up+1, down-1):
                # print(matrix[m-j-1][i])
                result.append(matrix[m-j-1][i])
            up += 1
            down -= 1
            left += 1
            right -= 1
        
        if (n%2 == 0 and m%2 == 0) or (m <= 3 and n <= 2) or (m <= 2 and n <= 3):
            pass

        else:
            if m >= n and n%2 == 1:
                for j in range(int(n/2) , m - int(n/2)):
                    # print(matrix[j][int(n/2)])
                    result.append(matrix[j][int(n/2)])

            elif m < n and m%2 == 1:
                for j in range(int(m/2) , n - int(m/2)):
                    # print(matrix[int(m/2)][j])
                    result.append(matrix[int(m/2)][j])

        return result


data = [[ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]]
# result = Solution().spiralOrder(data)

data = [[ 1, 2, 3, 4],
        [ 5, 6, 7, 8],
        [ 9,10,11,12],
        [13,14,15,16]]
# result = Solution().spiralOrder(data)

data = [[ 1, 2, 3, 4, 5],
        [ 6, 7, 8, 9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
# result = Solution().spiralOrder(data)

data = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9,10],
        [11, 12, 13, 14, 15]]
# result = Solution().spiralOrder(data)
# print(result)

data = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]]
# result = Solution().spiralOrder(data)
# print(result)

# result = Solution().spiralOrder([])
# print(result)

# data = [[2, 5],
#         [8, 4],
#         [0,-1]]
# result = Solution().spiralOrder(data)
# print(result)

# data = [[2, 5, 8],
#         [4, 0,-1]]
# result = Solution().spiralOrder(data)
# print(result)

# result = Solution().spiralOrder([[1],[2]])
# print(result)

# data = [[1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12],
#         [13,14,15,16],
#         [17,18,19,20]]
# result = Solution().spiralOrder(data)
# print(result)