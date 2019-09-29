class Solution(object):
    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """
        inf = int(1e20)
        rx, ry = x, y
        s = [(0, 0)]
        cx, cy = 0, 0
        for c in command:
            if c == 'U':
                cy += 1
            else:
                cx += 1
            s.append((cx, cy))
        crash = []
        inf = 1e18
        print(cx,cy)
        for ox, oy in obstacles:
            cc = inf
            for i, (x, y) in enumerate(s):
                if ox - x >= 0 and oy - y >= 0 and not (ox - x) % cx and not (oy - y) % cy and (ox - x) // cx == (oy - y) // cy:
                    crash.append((ox - x) // cx * len(command) + i)
                    break
        ox, oy = rx, ry
        reach = inf
        for i, (x, y) in enumerate(s):
            if ox - x >= 0 and oy - y >= 0 and not (ox - x) % cx and not (oy - y) % cy and (ox - x) // cx == (oy - y) // cy:
                reach = ((ox - x) // cx * len(command) + i)
                break
        print(reach, crash)

        return reach < (min(crash) if crash else inf)

command = "URR"
obstacles = []
x = 3
y = 2
res = Solution().robot(command, obstacles, x, y)
print(res)

command = "URR"
obstacles = [[2, 2]]
x = 3
y = 2
res = Solution().robot(command, obstacles, x, y)
print(res)

command = "URR"
obstacles = [[4, 2]]
x = 3
y = 2
res = Solution().robot(command, obstacles, x, y)
print(res)
