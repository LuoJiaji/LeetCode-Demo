class Solution(object):
    def domino(self, n, m, broken):
        """
        :type n: int
        :type m: int
        :type broken: List[List[int]]
        :rtype: int
        """
        b = [[0 for i in range(m + 2)] for j in range(n + 2)]
        for x, y in broken:
            b[x + 1][y + 1] = 1
        for x in range(0, n + 2):
            b[x][0] = 1
            b[x][-1] = 1
        for y in range(0, m + 2):
            b[0][y] = 1
            b[-1][y] = 1
        # print(b)

        def corner(x, y):
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            c = 0
            for dx, dy in d:
                if b[x + dx][y + dy]:
                    c += 1
            return c

        def put(x, y):
            b[x][y] = 1
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in d:
                if not b[x + dx][y + dy]:
                    b[x + dx][y + dy] = 1
                    break
            return

        ans = 0
        conti = True
        while conti:
            conti = False
            for x in range(n):
                for y in range(m):
                    if not b[x + 1][y + 1]:
                        c = corner(x + 1, y + 1)
                        if c == 4:
                            b[x + 1][y + 1] = 1
                            conti = True
                        elif c == 3:
                            put(x + 1, y + 1)
                            ans += 1
                            conti = True  
                    # print(b, conti, ans, c)

            if not conti:
                for x in range(n):
                    for y in range(m):
                        if not conti and not b[x + 1][y + 1]:
                        # if not b[x + 1][y + 1]:
                            c = corner(x + 1, y + 1)
                            if c == 4:
                                b[x + 1][y + 1] = 1
                                conti = True
                            elif c == 2 or c == 1:
                                put(x + 1, y + 1)
                                ans += 1
                                conti = True
                    # print(b)
        return ans

n = 2
m = 3
broken = [[1, 0], [1, 1]]
res = Solution().domino(n, m, broken)
print(res)

n = 3
m = 3
broken = []
res = Solution().domino(n, m, broken)
print(res)
