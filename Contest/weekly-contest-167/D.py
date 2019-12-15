class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        q = [[0,0]]
        state = [k]
        ans = 0
        n = len(grid)
        m = len(grid[0])
        if n == 1 and m == 1 and k <= 1:
            return 1
        while q:
            l = len(q)
            ans += 1
            curr_q = []
            curr_s = []
            print(q)
            for i,[x,y] in enumerate(q):
                print(x,y)
                s = state[i]
                if x+1 < m:
                    if grid[y][x+1] == 1 and s >= 1:
                        curr_q.append([x+1,y])
                        curr_s.append(s-1)
                        if [x+1, y] == [m-1, n-1]:
                            return ans
                    if grid[y][x+1] == 0:
                        curr_q.append([x+1,y])
                        curr_s.append(s)
                        if [x+1, y] == [m-1, n-1]:
                            return ans
                if x-1 > 0:
                    if grid[y][x-1] == 0:
                        curr_q.append([x-1,y])
                        curr_s.append(s)


                if y+1 < n:
                    if grid[y+1][x] == 1 and s >= 1:
                        curr_q.append([x, y+1])
                        curr_s.append(s-1)
                        if [x, y+1] == [m-1, n-1]:
                            return ans
                    if grid[y+1][x] == 0:
                        curr_q.append([x, y+1])
                        curr_s.append(s)
                        if [x, y+1] == [m-1, n-1]:
                            return ans
                if y-1 > 0:

                    if grid[y-1][x] == 0:
                        curr_q.append([x, y-1])
                        curr_s.append(s)

            q = curr_q
            state = curr_s

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
#  [1,1,1],
#  [1,0,0]]
# k = 1
# res = Solution().shortestPath(grid, k)
# print(res)

grid = [[0,1,0,0,0,1,0,0],[0,1,0,1,0,1,0,1],[0,0,0,1,0,0,1,0]]
k = 1
res = Solution().shortestPath(grid, k)
print(res)