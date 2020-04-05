class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from copy import deepcopy 
        def check (state):
            flag = True
            for i in state:
                if state[i] % 2 != 0:
                    flag = False
            return flag

        state = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        for i in s:
            if i in ['a', 'e','i','o','u']:
                state[i] += 1
        # print(state)
        # print(check(state))

        end = len(s)
        ans = 0
        curr_state = state
        # print('end',end)

        for right in reversed(range(1,end)):
            tmp_state = deepcopy(curr_state)
            if right == end - 1 or s[right + 1] in ['a', 'e','i','o','u']:
                for left in range(0, right+1):
                    if right - left + 1 < ans:
                        break

                    if left == 0:
                        if check(tmp_state):
                            ans = max(ans, right - left + 1)
                    # print(left, right)
                    if left - 1 >= 0 and s[left - 1] in ['a', 'e','i','o','u']:
                        tmp_state[s[left - 1]] -= 1
                        if check(tmp_state):
                            ans = max(ans, right - left + 1)
                        print(check(tmp_state), left, right, tmp_state, s[left:right+1], ans)
            
            if s[right] in ['a', 'e','i','o','u']:
                curr_state[s[right]] -= 1
                
        return ans
            
s = "eleetminicoworoep"
res = Solution().findTheLongestSubstring(s)
print(res)

s = "leetcodeisgreat"
res = Solution().findTheLongestSubstring(s)
print(res)

s = "bcbcbc"
res = Solution().findTheLongestSubstring(s)
print(res)

