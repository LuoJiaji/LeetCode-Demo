class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # print(prices)
        # i = 0
        # profile = 0
        # profile1 = 0
        # profile2 = 0
        # while i < len(prices)-1: 
        #     profile += max(0, prices[i + 1] - prices[i])
        #     if prices[i + 1] - prices[i] < 0 or i == len(prices)-2:
        #         if profile > profile1:
        #             profile2 = profile1
        #             profile1 = profile 
        #         elif profile > profile2:
        #             profile2 = profile 
        #         profile = 0 
        #     print(profile, prices[i+1] - prices[i], profile1, profile2)            
        #     i += 1
        # # print(profile)
        # return profile1 + profile2
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0, 0
        for i in prices:
            release2 = max(release2, hold2 + i)
            hold2 = max(hold2, release1 - i)
            release1 = max(release1, hold1 + i)
            hold1 = max(hold1, -i)
            print(release1, hold1, release2, hold2, i)
        return release2

# data = [3, 3, 5, 0, 0, 3, 1, 4]
# result = Solution().maxProfit(data)
# print(result)

data = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
result = Solution().maxProfit(data)
print(result)
