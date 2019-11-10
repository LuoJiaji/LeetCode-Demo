class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        count = 0
        s = 0
        for i in arr:
            s += i
            if s < 5000:
                count += 1
            else :
                break
        # print(count)


        return count



arr = [100,200,150,1000]
res = Solution().maxNumberOfApples(arr)
print(res)

arr = [900,950,800,1000,700,800]
res = Solution().maxNumberOfApples(arr)
print(res)
