class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        tmp = []
        curr = ''
        for i in range(l):
            if s[i] == '(':
                tmp.append(curr)
                curr = ''
            elif s[i]  == ')':
                curr = curr[::-1]
                if tmp != []:
                    curr = tmp.pop() + curr
            else:
                curr += s[i]
            # print(curr)

        return curr

s = "(abcd)"
res = Solution().reverseParentheses(s)
print(res)


s = "(u(love)i)"
res = Solution().reverseParentheses(s)
print(res)


s = "(ed(et(oc))el)"
res = Solution().reverseParentheses(s)
print(res)

s = "a(bcdefghijkl(mno)p)q"
res = Solution().reverseParentheses(s)
print(res)