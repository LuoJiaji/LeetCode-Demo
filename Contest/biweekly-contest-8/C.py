class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # left = [[-1 for _ in range(3)] for _ in range(len(colors))]
        # right = [[-1 for _ in range(3)] for _ in range(len(colors))]
        l = len(colors)

        left = [[-1] * 4 for _ in range(l)]
        right = [[-1] * 4 for _ in range(l)]

        l = len(colors)
        left[0][colors[0]-1] = 0 
        right[-1][colors[-1]-1] = 0

        i = 1
        while i < l:
            for j in range(3):
                left[i][j] = left[i-1][j]
                if left[i][j] >= 0:
                    left[i][j] = left[i][j] + 1
                if j == colors[i] - 1:
                    left[i][j] = 0
            i += 1

        i = 1
        while i < l:
            for j in range(3):
                right[l-1-i][j] = right[l-i][j]
                if right[l-1-i][j] >= 0:
                    right[l-1-i][j] = right[l-1-i][j] + 1
                if j == colors[l-1-i] - 1:
                    right[l-1-i][j] = 0
            i += 1
        # print(left)
        # print(right)

        ans = []
        for i in queries:
            # print(i)
            l = left[i[0]][i[1]-1]
            r = right[i[0]][i[1]-1]
            # print(l,r, min(l, r))
            if l == -1 and r == -1:
                ans.append(-1)              
            elif l == -1:
                ans.append(r)       
            elif r == -1:
                ans.append(l)               
            else:
                ans.append(min(l,r))
        # print(ans)
        return ans

colors = [1,1,2,1,3,2,2,3,3]
queries = [[1,3], [2,2], [6,1]]
result = Solution().shortestDistanceColor(colors, queries)
print(result)

colors = [1,2]
queries = [[0,3]]
result = Solution().shortestDistanceColor(colors, queries)
print(result)

colors = [2,1,2,2,1]
queries = [[1,1],[4,3],[1,3],[4,2],[2,1]]
result = Solution().shortestDistanceColor(colors, queries)
print(result)
