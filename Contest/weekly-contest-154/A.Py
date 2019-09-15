class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        word = 'balloon'
        d = {}
        for i in word:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        # print(d)

        counter = {}

        for i in text:
            if i in word:
                if i not in counter:
                    counter[i] = 1
                else:
                    counter[i] += 1
        # print(counter)

        ans = []
        for i in d:
            if i in counter:
                tmp = int(counter[i]/d[i])
                ans.append(tmp)
            else:
                ans.append(0)
            # print(i,tmp)

        # print(min(ans))
        return min(ans)


text = "nlaebolko"
res = Solution().maxNumberOfBalloons(text)
print(res)

text = "loonbalxballpoon"
res = Solution().maxNumberOfBalloons(text)
print(res)

text = "leetcode"
res = Solution().maxNumberOfBalloons(text)
print(res)