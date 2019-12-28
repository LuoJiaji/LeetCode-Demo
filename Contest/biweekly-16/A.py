class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        curr = -1
        for i in reversed(arr):
            # print(i)
            ans.append(curr)
            curr = max(curr, i)
        return ans[::-1]



arr = [17,18,5,4,6,1]
res = Solution().replaceElements(arr)
print(res)