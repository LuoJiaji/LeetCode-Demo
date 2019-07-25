
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        flag = [False] * len(nums)
        self.permuteUniqueRecu(result, flag, [], nums)
        print(result)
      

    def permuteUniqueRecu(self, result, flag, cur, nums):
        if len(cur) == len(nums):
            result.append(list(cur))

        else:
            for i in range(len(nums)):
                if flag[i] == False:
                    cur.append(nums[i])
                    flag[i] = True
                    self.permuteUniqueRecu(result, flag, cur, nums)
                    flag[i] = False
                    cur.pop()


data =  [1,2,3]
result = Solution().permuteUnique(data)
# print(result)