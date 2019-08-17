class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # print(prices)
        if prices == []:
            return 0
        min_p = prices[0]
        min_index = 0
        max_p = 0
        max_index = 0
        i = 0
        re = 0
        while i < len(prices):
            if prices[i] < min_p:
                min_p =  prices[i]
                max_p =  prices[i]
            
            if prices[i] > max_p:
                max_p =  prices[i]

            if max_p - min_p > re:
                re =  max_p - min_p
            i += 1
        # print(min_p, max_p)
        # print(re)
        return re


data = [7,1,5,3,6,4]
result = Solution().maxProfit(data)
print(result)
