class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        ans = set()
        l = len(text)
        for i in range(l):
            for j in range(i+2, l+1, 2):
                curr = text[i:j]
                # print(curr)
                l_curr = len(curr)
                a = curr[:int(l_curr/2)]
                b = curr[int(l_curr/2):]
                # print(a, b)
                if a == b:
                    # ans += 1
                    ans.add(curr)
        # print(ans)
        return len(ans)
        

text = "abcabcabc"
res = Solution().distinctEchoSubstrings(text)
print(res)

text = "leetcodeleetcode"
res = Solution().distinctEchoSubstrings(text)
print(res)