class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        alpha_dict = {}
        i = 0
        while i < 26:
            alpha_dict[keyboard[i]] = i
            i += 1
         
        # print(keyboard,word)
        # print(alpha_dict)
        
        pre = 0
        l = 0
        for i in word:
            l += abs(alpha_dict[i] - pre)
            pre = alpha_dict[i]
        # print(l)
        return l

keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"
result = Solution().calculateTime(keyboard, word)
print(result)

keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
result = Solution().calculateTime(keyboard, word)
print(result)