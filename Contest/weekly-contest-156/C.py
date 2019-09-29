class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        curr = []
        ttl = []
        # curr.append(s[0])
        for i in range(len(s)):
            # print(s[i], curr, ttl)
            if curr == [] or curr[-1] == s[i]:
                curr.append(s[i])
                if len(curr) == k:
                    curr = []
                    if len(ttl) > 0:
                        curr = ttl.pop()
            else:
                ttl.append(curr)
                curr = []
                curr.append(s[i])
            # print(curr,ttl)
        # print(curr, ttl)

        ans = ''
        for i in ttl:
            for j in i :
                ans += j
        for i in curr:
            ans += i
        # print(ans)
        return ans

s = "abcd"
k = 2
res = Solution().removeDuplicates(s,k)
print(res)

s = "deeedbbcccbdaa"
k = 3
res = Solution().removeDuplicates(s,k)
print(res)

s = "pbbcggttciiippooaais"
k = 2
res = Solution().removeDuplicates(s,k)
print(res)