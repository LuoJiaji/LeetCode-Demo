
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        flag = [False] * len(nums)
        self.permuteUniqueRecu(result, flag, [], nums)
        return result
        

    def permuteUniqueRecu(self, result, flag, cur, nums):
        pre = '0'
        if len(cur) == len(nums):
            result.append(list(cur))

        else:
            for i in range(len(nums)):
                if flag[i] or (i > 0 and nums[i-1] == nums[i] and not flag[i-1]):
                    continue
                cur.append(nums[i])
                flag[i] = True
                self.permuteUniqueRecu(result, flag, cur, nums)
                flag[i] = False
                cur.pop()



data =  [1,1,2]
result = Solution().permuteUnique(data)
print(result)
