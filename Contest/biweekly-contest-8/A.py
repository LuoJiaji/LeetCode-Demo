class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        count = []
        i = 0
        pre = S[0]
        tmp = 0
        while  i <= len(S)-1:

            if S[i] == pre:
                tmp += 1
            else:
                # print(tmp)
                count.append(tmp)
                tmp = 1
                pre = S[i]
                
                # print(tmp)
            i += 1
        # print(tmp)
        count.append(tmp)
        # print(count)
        ans = 0
        for i in count:
            ans += int((1 + i)*i /2)
        # print(ans)

        return ans



S = "aaaba"
result = Solution().countLetters(S)
print(result)

S = "aaaaaaaaaa"
result = Solution().countLetters(S)
print(result)