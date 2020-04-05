class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        s = sum(digits)
        m = s % 3
        # print(s%3)

        if max(digits) == 0:
            return '0'

        if m == 0:
            digits = sorted(digits, reverse=True)
            ans = ''
            for i in digits:
                ans += str(i)
            return ans
        
        list_mod0 = []
        list_mod1 = []
        list_mod2 = []

        for i in digits:
            if i % 3 == 0:
                list_mod0.append(i)
            if i % 3 == 1:
                list_mod1.append(i)
            if i % 3 == 2:
                list_mod2.append(i)
        # print(list_mod1)
        # print(list_mod2)

        list_mod1 = sorted(list_mod1, reverse=True)
        list_mod2 = sorted(list_mod2, reverse=True)
        if m == 1:
            if list_mod1 == []:
                if len(list_mod2) < 2:
                    return ''
                else:
                    list_mod2 = list_mod2[:-2]
            else:
                list_mod1 = list_mod1[:-1]
        
        if m == 2:
            if list_mod2 == []:
                if len(list_mod1) < 2:
                    return ''
                else:
                    list_mod1 = list_mod1[:-2]
            else:
                list_mod2 = list_mod2[:-1]
        # print(list_mod0, list_mod1, list_mod2)
        digits = list_mod0 + list_mod1 + list_mod2
        
        digits = sorted(digits, reverse=True)
        ans = ''
        for i in digits:
            ans += str(i)

        return ans


digits = [8,1,9]
res = Solution().largestMultipleOfThree(digits)
print(res)

digits = [8,6,7,1,0]
res = Solution().largestMultipleOfThree(digits)
print(res)

digits = [1]
res = Solution().largestMultipleOfThree(digits)
print(res)

digits = [0,0,0,0,0,0]
res = Solution().largestMultipleOfThree(digits)
print(res)

digits = [1,1,1,2]
res = Solution().largestMultipleOfThree(digits)
print(res)


