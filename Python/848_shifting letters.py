class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        ans = ''
        l = len(S)
        cum = 0
        for i in reversed(range(l)):
            cum += shifts[i]
            cum = cum % 26
            tmp = (ord(S[i]) - ord('a') + cum ) % 26 + ord('a')
            ans = chr(tmp) + ans

        # print(ans)
        return ans

S = "abc"
shifts = [3,5,9]
res = Solution().shiftingLetters(S, shifts)
print(res)