class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        ans = []
        ans.append(text)
        # curr = ans
        while 1:
            curr = []
            for i,j in synonyms:
                for s in ans:
                    sl = s.split(' ')
                    if i in sl:
                        for ind in range(len(sl)):
                            if sl[ind] == i:
                                sl[ind] = j
                                tmp = ' '.join(sl)
                                if tmp not in ans and tmp not in curr:
                                    curr.append(tmp)
                                sl[ind] = i
                    if j in sl:
                        for ind in range(len(sl)):
                            if sl[ind] == j:
                                sl[ind] = i
                                tmp = ' '.join(sl)
                                if tmp not in ans and tmp not in curr:
                                    curr.append(tmp)
                                sl[ind] = j

            ans += curr
            if curr == []:
                break
        # print(ans)
        # print(len(ans))
        ans.sort()
        # print(ans)
        # print(len(ans))
        return ans

synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"
res = Solution().generateSentences(synonyms, text)
print(res)
print(len(res))
synonyms = [["a","QrbCl"]]
text = "d QrbCl ya ya NjZQ"
res = Solution().generateSentences(synonyms, text)
print(res)
print(len(res))

synonyms = [["v","yr"]]
text = "v v v v yZ"
res = Solution().generateSentences(synonyms, text)
print(res)
print(len(res))