# /*
#  * @Author: JJ Luo 
#  * @Date: 2019-07-27 17:06:50 
#  * @Last Modified by:   JJ Luo 
#  * @Last Modified time: 2019-07-27 17:06:50 
#  */


import copy

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if s == "" or words == []:
            return []

        m = len(s)
        n = len(words[0])
        # print(m, n)
        result = []
        for starter in range(m - n + 1):
            comp = s[starter : starter + n]
            i = 1
            W = copy.copy(words)
            # print(comp)
            while comp in W:
                print(starter, comp, W)
                W.remove(comp)
                comp = s[starter + i*n : starter + (i+1)*n]
                print(starter, comp, W)
                i += 1
            if W == []:
                # print(starter)  
                result.append(starter)

        # print(result)
        return result



# s = "barfoothefoobarman"
# words = ["foo","bar"]
# result = Solution().findSubstring(s, words)
# print(result)

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# result = Solution().findSubstring(s, words)
# print(result)

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
result = Solution().findSubstring(s, words)
print(result)


# s = ""
# words = []
# result = Solution().findSubstring(s, words)
# print(result)

# s = "a"
# words = []
# result = Solution().findSubstring(s, words)
# print(result)