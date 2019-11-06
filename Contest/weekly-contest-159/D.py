class Solution:
    def jobScheduling(self, startTime, endTime, profit):

        # pair = []
        # for i in range(len(startTime)):
        #     pair.append([endTime[i], startTime[i], profit[i]])        
        # print(pair)
        # pair.sort()
        # print(pair)

        dp = [0] * (max(endTime) + 1)

        for i in range(1, max(endTime) + 1):
            dp[i] = dp[i-1]
            if i in endTime:
               for j in range(len(endTime)):
                   if endTime[j] == i:
                       dp[i] = max(dp[i], dp[startTime[j]] + profit[j])
        # print(dp)
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

