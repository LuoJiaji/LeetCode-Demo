class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = sum(nums)
        if ans % 3 == 0:
            return ans
        nums.sort()

        tmp1 = []
        for i in nums:
            if i % 3 == 1:
                tmp1.append(i)
            if len(tmp1) == 2:
                break
        tmp2 = []
        for i in nums:
            if i % 3 == 2:
                tmp2.append(i)
            if len(tmp2) == 2:
                break
        max_ans = 0
        
        if ans % 3 == 1:
            if tmp1 != []:
                max_ans = max(max_ans, ans - tmp1[0])
            if len(tmp2) == 2:
                max_ans = max(max_ans, ans - sum(tmp2))

        if ans % 3 == 2:
            if len(tmp1) == 2:
                max_ans = max(max_ans, ans - sum(tmp1))
            if tmp2 != []:
                max_ans = max(max_ans, ans - tmp2[0])

        # print(max_ans)
        return max_ans

nums = [3,6,5,1,8]
res = Solution().maxSumDivThree(nums)
print(res)

nums = [4]
res = Solution().maxSumDivThree(nums)
print(res)

nums = [1,2,3,4,4]
res = Solution().maxSumDivThree(nums)
print(res)

nums = [2,6,2,2,7]
res = Solution().maxSumDivThree(nums)
print(res)

nums = [2,3,36,8,32,38,3,30,13,40]
res = Solution().maxSumDivThree(nums)
print(res)