class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        next = []
        l = len(arr)
        while True:
            next.append(arr[0])
            for i in range(1,l-1):
                if arr[i-1] < arr[i] and  arr[i] > arr[i+1]:
                    next.append(arr[i] - 1)
                elif arr[i-1] > arr[i] and arr[i] < arr[i+1]:
                    next.append(arr[i] + 1)
                else:
                    next.append(arr[i])
            next.append(arr[-1])

            if arr == next:
                return next
            else:
                arr = next
                next = []

data = [6,2,3,4]
res = Solution().transformArray(data)
print(res)

data = [1,6,3,4,3,5]
res = Solution().transformArray(data)
print(res)
