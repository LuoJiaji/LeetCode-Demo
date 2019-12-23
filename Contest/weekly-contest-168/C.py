class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        l = len(s)
        mp = {}
        for i in range(l):
            t = {}
            tt = ''
            for j in range(i, min(i + maxSize, l)):
                if s[j] not in t:
                    t[s[j]] = 1
                else:
                    t[s[j]] += 1
                tt += s[j]
            # print(tt)
                if len(t) <= maxLetters and minSize <= len(tt) <= maxSize :
                    if tt in mp:
                        mp[tt] += 1
                    else:
                        mp[tt] = 1
        # print(mp)
        # print(mp[max(mp, key = mp.get)])
        if mp == {}:
            return 0
        ans = mp[max(mp, key = mp.get)]
        return ans
                
s = "aababcaab"; maxLetters = 2; minSize = 3; maxSize = 4
res = Solution().maxFreq(s, maxLetters, minSize, maxSize)
print(res)

s = "aaaa"; maxLetters = 1; minSize = 3; maxSize = 3
res = Solution().maxFreq(s, maxLetters, minSize, maxSize)
print(res)

s = "aabcabcab"; maxLetters = 2; minSize = 2; maxSize = 3
res = Solution().maxFreq(s, maxLetters, minSize, maxSize)
print(res)

s = "abcde"; maxLetters = 2; minSize = 3; maxSize = 3
res = Solution().maxFreq(s, maxLetters, minSize, maxSize)
print(res)

s = "aaaaacbc"
maxLetters = 2
minSize = 4
maxSize = 6
res = Solution().maxFreq(s, maxLetters, minSize, maxSize)
print(res)

# a = {'a':1, 'b':6, 'c':2}
# print(len(a))
# print(max(a, key=a.get))