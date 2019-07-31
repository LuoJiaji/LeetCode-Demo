class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        l = len(nums)
        result = []
        for i in range(1,l+1):
            result_sub = []
            flag = [False]*len(nums)
            self.subsetsRecu(flag, [], nums, i, 0, result_sub)
            # print(result)
            result.append(result_sub)
            # print(result_sub)
        # print(result)
        # print(len(result))

        ans = []
        for i in result:
            for j in i:
                # print(j)
                ans.append(j)
        ans.append([])
        # print(ans)
        return ans





    def subsetsRecu(self, flag, curr, nums, k, start, result):
        if len(curr) == k:
            # print(curr)
            result.append(list(curr)) 

        for i in range(start, len(nums)):
            if flag[i] == False:
                curr.append(nums[i])
                flag[i] = True
                self.subsetsRecu(flag, curr, nums, k, i, result)
                curr.pop()
                flag[i] = False


data = [1,2,3]
result = Solution().subsets(data)
print(result)