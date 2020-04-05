class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = sorted(s)
        # print(s)
        res = ''

        while s != []:
            curr = s[0]
            for i in s:
                if i != curr[-1]:
                    curr += i
            # print(s, curr)
            for i in curr:        
                s.remove(i)
            # print(curr)

            res += curr
            if s == []:
                break
            curr = s[-1]
            for i in reversed(s):
                if i != curr[-1]:
                    curr += i
            # print(s, curr)
            for i in curr:
                s.remove(i)
            # print(curr)
            res += curr

        return res


s = "aaaabbbbcccc"
res = Solution().sortString(s)
print(res)

s = "rat"
res = Solution().sortString(s)
print(res)

s = "leetcode"
res = Solution().sortString(s)
print(res)


s = "spo"
res = Solution().sortString(s)
print(res)