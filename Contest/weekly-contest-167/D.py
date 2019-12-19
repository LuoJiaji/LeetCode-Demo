class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        q = {(0,0):k}
        ans = 0
        n = len(grid)
        m = len(grid[0])
        print(m,n)
        for i in grid:
            print(i)
        if n == 1 and m == 1 and k <= 1:
            return 0
        while q:
            l = len(q)
            ans += 1
            curr_q = {}
            print(q)
            for x,y in q:
                # print(x,y)
                s = q[(x,y)]
                if x+1 < m:
                    if grid[y][x+1] == 1 and s >= 1:
                        if (x+1,y) in curr_q:
                            curr_q[(x+1,y)] = max(curr_q[(x+1,y)], s-1)
                        else:
                            curr_q[(x+1,y)] =s-1
                        if [x+1, y] == [m-1, n-1]:
                            return ans
                    if grid[y][x+1] == 0:
                        if (x+1,y) in curr_q:
                            curr_q[(x+1,y)] = max(curr_q[(x+1,y)], s)
                        else:
                            curr_q[(x+1,y)] = s
                        if [x+1, y] == [m-1, n-1]:
                            return ans
                if x-1 >= 0 and grid[y][x-1] == 0:
                        if (x-1,y) in curr_q:
                            curr_q[(x-1,y)] = max(curr_q[(x-1,y)], s)
                        else:
                            curr_q[(x-1,y)] = s

                if y+1 < n:
                    if grid[y+1][x] == 1 and s >= 1:
                        if (x, y+1) in curr_q:
                            curr_q[(x, y+1)] = max(curr_q[(x, y+1)], s-1)
                        else:
                            curr_q[(x, y+1)] = s-1
                        if [x, y+1] == [m-1, n-1]:
                            return ans
                    if grid[y+1][x] == 0:
                        if (x, y+1) in curr_q:
                            curr_q[(x, y+1)] = max(curr_q[(x, y+1)], s)
                        else:
                            curr_q[(x, y+1)] = s

                        if [x, y+1] == [m-1, n-1]:
                            return ans
                if y-1 >= 0 and grid[y-1][x] == 0:
                        if (x, y-1) in curr_q:
                            curr_q[(x, y-1)] = max(curr_q[(x, y-1)], s)
                        else:
                            curr_q[(x, y-1)] = s
            q = curr_q
        return -1

# grid = [[0,0,0],
#         [1,1,0],
#         [0,0,0],
#         [0,1,1],
#         [0,0,0]]
# k = 1
# res = Solution().shortestPath(grid, k)
# print(res)

# grid = [[0,1,1],
#         [1,1,1],
#         [1,0,0]]
# k = 1
# res = Solution().shortestPath(grid, k)
# print(res)

# grid = [[0,1,0,0,0,1,0,0],[0,1,0,1,0,1,0,1],[0,0,0,1,0,0,1,0]]
# k = 1
# res = Solution().shortestPath(grid, k)
# print(res)

grid = [[0,0,1,0,1,1,1,0],[1,1,0,1,0,1,0,0],[1,1,0,0,1,0,1,1],[1,1,0,1,0,1,0,0],[1,0,0,1,0,1,0,1],[0,0,1,1,1,0,0,1],[0,1,0,1,1,1,1,0],[1,0,0,0,1,1,1,0],[0,0,0,1,0,0,0,1],[1,0,1,0,0,0,1,0],[1,0,1,0,1,1,1,1],[1,1,1,0,0,0,0,1],[0,0,1,1,1,1,0,0],[0,1,0,1,0,1,0,1],[1,1,0,0,1,0,0,0],[0,1,1,1,0,0,1,1],[0,1,0,0,0,0,1,0],[1,1,1,0,1,0,0,0],[1,0,1,1,1,1,1,0],[0,1,0,1,0,0,1,0],[1,1,1,1,0,1,0,1],[0,0,0,0,0,0,1,1],[0,1,0,0,0,0,1,1],[1,1,1,0,0,0,1,1],[0,1,0,0,1,0,0,1],[1,0,0,1,0,1,0,0],[0,0,0,0,1,1,0,1],[0,0,1,0,1,0,1,0],[0,1,1,1,1,0,1,0]]
k = 3
res = Solution().shortestPath(grid, k)
print(res)