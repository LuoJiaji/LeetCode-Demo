class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        print(nums, k)
        s = [0] * 100005
        c = [0] * 100005
        ans = 0
        c[0] += 1
        l = len(nums)
        for i in range(l):
            if nums[i]&1 :
                s[i] = s[i-1] + 1
            else:
                s[i] = s[i-1]
            c[s[i]] += 1
            ans += c[s[i]-k]
            
            print(i, s[0:12], c[0:12], i, s[i], ans)
        return ans

nums = [1,1,2,1,1]
k = 3
res = Solution().numberOfSubarrays(nums, k)
print(res)

nums = [2,4,6]
k = 1
res = Solution().numberOfSubarrays(nums, k)
print(res)

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
res = Solution().numberOfSubarrays(nums, k)
print(res)
