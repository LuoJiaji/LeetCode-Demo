class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def get_pos(i):
            p = ord(i) - ord('A')
            x = p % 6
            y = p // 6
            return x,y

        l = len(word)
        ans = 100000
        for i in range(1, l):
            f1_x, f1_y = get_pos(word[0])
            f2_x, f2_y = get_pos(word[i])
            curr_dis = 0
            for ind in range(l):
                dp = [[0] * 2 for _ in range(l)]
                print(dp)
                x,y = get_pos(word[ind])
                if ind < i:
                    curr_dis += abs(f1_x - x) + abs(f1_y - y)
                    f1_x = x
                    f1_y = y
                    dp[ind][0] = curr_dis
                    if abs(f1_x - x) + abs(f1_y - y) < abs(f2_x - x) + abs(f2_y - y):
                        curr_dis += abs(f1_x - x) + abs(f1_y - y)
                        f1_x = x
                        f1_y = y
                    else:
                        curr_dis += abs(f2_x - x) + abs(f2_y - y)
                        f2_x = x
                        f2_y = y
            ans = min(ans, curr_dis)
            # print(curr_dis)
        return ans




word = "CAKE"
res = Solution().minimumDistance(word)
print(res)

word = "HAPPY"
res = Solution().minimumDistance(word)
print(res)

word = "NEW"
res = Solution().minimumDistance(word)
print(res)

word = "YEAR"
res = Solution().minimumDistance(word)
print(res)