class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = 0
        l = len(s)
        sp = []
        while p < l:
            if p+2 < l and s[p+2] == '#':
                sp.append(s[p:p+2])
                p += 3
            else:
                sp.append(s[p])
                p += 1
        # print(sp)

        ans = ''
        for i in sp:
            ans += chr(int(i)+96)
        return ans


        

s = "10#11#12"
res = Solution().freqAlphabets(s)
print(res)

s = "1326#"
res = Solution().freqAlphabets(s)
print(res)

s = "25#"
res = Solution().freqAlphabets(s)
print(res)

s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
res = Solution().freqAlphabets(s)
print(res)