class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        mp = {}
        for word in words:
            st = set(word)
            s = 0
            for ch in st:
                s |= 1 << (ord(ch) - ord('a'))
            mp[s] = mp.get(s, 0) + 1
        ans = [0] * len(puzzles)
        for idx, p in enumerate(puzzles):
            for i in range(1 << 6):
                s = 1 << (ord(p[0]) - ord('a'))
                for j in range(6):
                    if (i & (1 << j)) > 0:
                        s |= (1 << (ord(p[j + 1]) - ord('a')))
                ans[idx] += mp.get(s, 0)
        return ans
        
words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
result = Solution().findNumOfValidWords(words, puzzles)
print(result)
