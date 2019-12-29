class Solution(object):
    def isSolvable(self, words, result):
        """
        :type words: List[str]
        :type result: str
        :rtype: bool
        """
        import copy
        used = []
        flag = False
        def check(numlist, alpha, words, result):
            # pass
            nums = []
            for w in words:
                tmp = ''
                for a in w:
                    ind = alpha.index(a)
                    tmp += str(numlist[ind])
                nums.append(tmp)
            res = ''
            for i in result:
                ind = alpha.index(i)
                res += str(numlist[ind])
            s = 0
            for num in nums:
                s += int(num)
            if s == int(res):
                flag = True
            # print(nums, res)

        def dfs(alpha, i, used, numlist):
            numlist = copy.deepcopy(numlist)
            used = copy.deepcopy(used)
            # print(numlist, used)
            if i == len(alpha):
                # print()
                # res = check(numlist)
                # pass
                # print(i, len(alpha), numlist)
                check(numlist, alpha, words, result)
                # return

            for n in range(10):
                # print(n, used)
                if n not in used:
                    new_used = used + [n]
                    new_numlist = numlist + [n]
                    dfs(alpha, i+1, new_used, new_numlist)

        alpha = result
        for w in words:
            alpha += w
        alpha = list(set(alpha))
        print(alpha) 
        dfs(alpha, 0, [], [])
        return flag

words = ["SEND","MORE"]
result = "MONEY"
res = Solution().isSolvable(words, result)
print(res)