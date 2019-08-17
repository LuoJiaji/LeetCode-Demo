class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # print(prices)
        i = 0
        # min_price = 0
        # max_price = 0
        profile = 0
        while i < len(prices)-1:
            profile += max(0, prices[i + 1] - prices[i]) 
            # print(profile, prices[i] - prices[i-1])            
            i += 1
        # print(profile)
        return profile

data = [7, 1, 5, 3, 6, 4]
result = Solution().maxProfit(data)
print(result)

data =  [1,2,3,4,5]
result = Solution().maxProfit(data)
print(result)

data =  [7,6,4,3,1]
result = Solution().maxProfit(data)
print(result)