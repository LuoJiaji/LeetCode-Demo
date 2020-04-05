class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        if n % 2 == 1:
            ans = 'a'*n
        else:
            ans = 'a'*(n-1) + 'b'

        return ans

res = Solution().generateTheString(4)
print(res)

