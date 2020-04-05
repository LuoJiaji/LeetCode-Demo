class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        l = len(light)
        ans = 0
        right = 0
        curr_min = light[0]
        curr_max = 0
        for i in range(1,l+1):
            right = max(right, light[i-1])
            curr_min = min(curr_min, light[i-1])
            curr_max = max(curr_max, light[i-1])
            if right == i:
                tmp = light[:i]
                if curr_max == len(tmp) and curr_min == 1:
                    ans += 1
        # print(ans)
        return ans


light = [2,1,3,5,4]
res = Solution().numTimesAllBlue(light)
print(res)

light = [3,2,4,1,5]
res = Solution().numTimesAllBlue(light)
print(res)

light = [4,1,2,3]
res = Solution().numTimesAllBlue(light)
print(res)

light = [2,1,4,3,6,5]
res = Solution().numTimesAllBlue(light)
print(res)

light = [1,2,3,4,5,6]
res = Solution().numTimesAllBlue(light)
print(res)


