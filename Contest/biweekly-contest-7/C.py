
from heapq import *
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """    
        res = 0
        heapify(sticks)
        print(sticks)
        while len(sticks) > 1:
            s1 = heappop(sticks)
            s2 = heappop(sticks)
            res += s1 + s2
            heappush(sticks, s1 + s2)
        return res

sticks = [2,4,3]
result = Solution().connectSticks(sticks)
print(result)

sticks = [1,8,3,5]
result = Solution().connectSticks(sticks)
print(result)
