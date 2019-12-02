class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        ans = [0,0]
        if tomatoSlices - 2* cheeseSlices < 0 or 4 * cheeseSlices - tomatoSlices < 0 or (tomatoSlices - 2* cheeseSlices) % 2 != 0:
            return []
        else:
            ans [0] =  int((tomatoSlices - 2* cheeseSlices) / 2)
            ans [1] =  int(cheeseSlices - ans[0])
        
            return ans


tomatoSlices = 16; cheeseSlices = 7
res = Solution().numOfBurgers(tomatoSlices, cheeseSlices)
print(res)

tomatoSlices = 17; cheeseSlices = 4
res = Solution().numOfBurgers(tomatoSlices, cheeseSlices)
print(res)

tomatoSlices = 4; cheeseSlices = 17
res = Solution().numOfBurgers(tomatoSlices, cheeseSlices)
print(res)

tomatoSlices = 0; cheeseSlices = 0
res = Solution().numOfBurgers(tomatoSlices, cheeseSlices)
print(res)

tomatoSlices = 2; cheeseSlices = 1
res = Solution().numOfBurgers(tomatoSlices, cheeseSlices)
print(res)

res = Solution().numOfBurgers(2385088,164763)
print(res)