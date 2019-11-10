class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in arr1:
            if i in arr2 and i in arr3:
                ans.append(i)
        return ans

        


arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

res = Solution().arraysIntersection(arr1, arr2, arr3)
print(res)