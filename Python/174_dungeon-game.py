class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        curr = [[0 for _ in dungeon[0]] for _ in dungeon]
        # min_blod = [[0 for _ in dungeon[0]] for _ in dungeon]
        # print(dungeon)
        # print(curr)
        # print(min_blod)

        x = 0
        y = 0
        N = len(dungeon[0])
        M = len(dungeon)
        curr = 0
        min_blod = 0
        res =  []
        self.next_step(x,y, N, M, curr, dungeon, 0, res)
        # print(res)
        ans = max(res)
        # print(ans)

        if ans > 0:
            return 1
        else:
            return abs(ans) + 1 


    def next_step(self,x, y, N, M, curr, dungeon, min_blod, res):
        curr += dungeon[y][x]
        min_blod = min(min_blod, curr)

        if x == N-1 and y == M-1:
            # print(curr, min_blod)
            res.append(min_blod)

        if x < N-1:
            self.next_step(x+1, y, N, M, curr, dungeon, min_blod, res)
        if y < M-1:
            self.next_step(x, y+1, N, M, curr, dungeon, min_blod, res)

            

        




data = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
result = Solution().calculateMinimumHP(data)
print(result)

data = [[100]]
result = Solution().calculateMinimumHP(data)
print(result)

data = [[1,-4,5,-99],[2,-2,-2,-1]]
result = Solution().calculateMinimumHP(data)
print(result)

data = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
result = Solution().calculateMinimumHP(data)
print(result)