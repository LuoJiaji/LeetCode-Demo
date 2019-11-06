class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        times = set()
        n = len(startTime)
        for i in range(n):
            times.add(startTime[i])
            times.add(endTime[i])
        times = sorted(list(times))
        print(times)
        pair = zip(times, range(len(times)))
        d = {k: v for k, v in pair}
        # get_time = {v: k for k, v in pair}
        print(d)
        # print(get_time)
        l = len(times)
        dp = [0 for i in range(l)]
        back = [[] for i in range(l)]
        for i in range(n):
            x, y, p = startTime[i], endTime[i], profit[i]
            x, y = d[x], d[y]
            back[y].append([x, p])

        print(back)
        for i in range(l):
            if i > 0:
                dp[i] = dp[i - 1]
                for u, p in back[i]:
                    dp[i] = max(dp[i], dp[u] + p)
        print(dp)
        return dp[-1]

# startTime = [1,2,3,3]
# endTime = [3,4,5,6]
# profit = [50,10,40,70]
# res = Solution().jobScheduling(startTime, endTime, profit)
# print(res)

# startTime = [1,2,3,4,6]
# endTime = [3,5,10,6,9]
# profit = [20,20,100,70,60]
# res = Solution().jobScheduling(startTime, endTime, profit)
# print(res)

# startTime = [1,1,1]
# endTime = [2,3,4]
# profit = [5,6,4]
# res = Solution().jobScheduling(startTime, endTime, profit)
# print(res)

startTime = [43,13,36,31,40,5,47,13,28,16,2,11]
endTime = [44,22,41,41,47,13,48,35,48,26,21,39]
profit = [8,20,3,19,16,8,11,13,2,15,1,1]
res = Solution().jobScheduling(startTime, endTime, profit)
print(res)