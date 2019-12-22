class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        begin = 0
        end = 1
        # print
        ans = len(s)
        sub_s = []
        flag = False
        while begin < end:
            # print(s[end], s[begin: end])
            if len(set(s[begin: end])) <= maxLetters and end < len(s):
                end += 1
                # if len(set(s[begin: end])) == maxLetters and s[end] in s[begin: end]:              
            else:
                begin += 1
            # print('tmp',s[begin: end])
            if len(set(s[begin: end])) <= maxLetters:
                # print(s[begin: end])
                # sub_s.append(s[begin: end])
                i = 0
                while begin + i < end:
                    if len(set(s[begin + i : end])) <= maxLetters and minSize <= len(s[begin + i : end]) <= maxSize:
                        sub_s.append(s[begin+i: end])
                    i += 1
                if end == len(s):
                    flag = True
            if flag:
                break
            # print(sub_s)
        # print(sub_s)
        ans = 0
        for i in sub_s:
            ans = max(sub_s.count(i), ans)
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