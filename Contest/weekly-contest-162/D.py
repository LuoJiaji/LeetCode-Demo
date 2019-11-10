class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        import copy
        words_score = [0 for _ in words]
        self.ans = 0
        for i in range(len(words)):
            for j in words[i]:
                words_score[i] += score[ord(j)-ord('a')]
        # print(words_score)

        def check(words, i, letters, s):
            letters = copy.deepcopy(letters)
            # print(i, letters)
            if i == len(words):
                self.ans = max(s, self.ans)
                return
            
            check(words, i+1, letters, s)
            flag = True
            for c in words[i]:
                if c not in letters:
                    flag = False
                else:
                    letters.remove(c)
            if flag:
                check(words, i+1, letters, s + words_score[i])
            
            
        for i in range(len(words)):
            check(words, i+1, letters, 0)
            
            flag = True
            for c in words[i]:
                if c not in letters:
                    flag = False
                else:
                    letters.remove(c)
            if flag:
                check(words, i+1, letters, words_score[i])

        # print(self.ans)
        return self.ans

letters = ["a","a","c","d","d","d","g","o","o"]

# letters.pop("a")
# print(letters)

words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
res = Solution().maxScoreWords( words, letters, score)
print(res)

words = ["xxxz","ax","bx","cx"]
letters = ["z","a","b","c","x","x","x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
res = Solution().maxScoreWords( words, letters, score)
print(res)

words = ["leetcode"]
letters = ["l","e","t","c","o","d"]
score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
res = Solution().maxScoreWords( words, letters, score)
print(res)