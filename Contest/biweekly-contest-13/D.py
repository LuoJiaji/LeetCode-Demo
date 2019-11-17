class Solution(object):
    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        dp = [0] * 1050
        dp[2] = 1
        dp[4] = 2
        i = 6
        while i <= num_people:
            A = 2
            B = i-2-2
            ans = 0
            while A <= i-4:
                ans += dp[A] * dp[B]
                A += 2
                B -= 2
            ans += dp[i-2] * 2
            dp[i] = ans
            i += 2

        dp = [0] * 1050
        dp[2] = 1
        dp[4] = 2
        i = 6
        while i <= num_people:
            A = 2
            B = i-2-2
            ans = 0
            while A <= i-4:
                ans += dp[A] * dp[B]
                A += 2
                B -= 2
            ans += dp[i-2] * 2
            dp[i] = ans
            i += 2

        return dp[num_people] % 1000000007            


num_people = 2
res = Solution().numberOfWays(num_people)
print(res)

num_people = 4
res = Solution().numberOfWays(num_people)
print(res)

num_people = 6
res = Solution().numberOfWays(num_people)
print(res)

num_people = 8
res = Solution().numberOfWays(num_people)
print(res)

num_people = 140
res = Solution().numberOfWays(num_people)
print(res)