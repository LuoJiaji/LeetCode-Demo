class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if nums == []:
            reutrn []
        nums.sort()
        # print(nums)
        maj_num = int(len(nums)/3)
        # print(maj_num)
        res = []
        counter = 1

        if counter > maj_num:
            res.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                counter += 1
            else:
                counter = 1

            if counter > maj_num and nums[i] not in res:
                res.append(nums[i])

        # print(res)
        return res
            

data = [3,2,3]
result = Solution().majorityElement(data)
print(result)

data = [1,1,1,3,3,2,2,2]
result = Solution().majorityElement(data)
print(result)

data = [1]
result = Solution().majorityElement(data)
print(result)