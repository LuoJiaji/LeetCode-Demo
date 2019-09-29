class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = {}
        for i in arr:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1

        tmp = []

        for i in cnt:
            if cnt[i] in tmp:
                return False
            else:
                tmp.append(cnt[i])
        return True


arr = [1,2,2,1,1,3]
res = Solution().uniqueOccurrences(arr)
print(res)

arr = [1,2]
res = Solution().uniqueOccurrences(arr)
print(res)

arr = [-3,0,1,-3,1,1,1,-3,10,0]
res = Solution().uniqueOccurrences(arr)
print(res)