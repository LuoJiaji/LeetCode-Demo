class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # print(s)
        # print(s.lower())
        # print(s[0].isalnum())

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        

data = "A man, a plan, a canal: Panama"
result = Solution().isPalindrome(data)
print(result)
