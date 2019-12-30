# class Solution(object):
#     def isSolvable(self, words, result):
#         """
#         :type words: List[str]
#         :type result: str
#         :rtype: bool
#         """
#         # used = []
#         # flag = False
#         def check(numlist, alpha, words, result):
#             # pass
#             flag = False
#             nums = []
#             for w in words:
#                 tmp = ''
#                 for a in w:
#                     ind = alpha.index(a)
#                     tmp += str(numlist[ind])
#                 nums.append(tmp)
#             res = ''
#             for i in result:
#                 ind = alpha.index(i)
#                 res += str(numlist[ind])
#             s = 0
#             for num in nums:
#                 s += int(num)
#             if s == int(res):
#                 flag = True
#                 print(nums, res)
#             return flag
#             # print(nums, res)

#         def dfs(alpha, i, used, numlist, cantzero):
#             # numlist = copy.deepcopy(numlist)
#             # used = copy.deepcopy(used)
#             # print(numlist, used)
#             if i == len(alpha):
#                 # print(i, len(alpha), numlist)
#                 res = check(numlist, alpha, words, result)
#                 return res

#             for n in range(10):
#                 # print(n, used)
#                 if n == 0 and alpha[i] in cantzero:
#                     continue
#                 if n not in used:
#                     # new_used = used + [n]
#                     # new_numlist = numlist + [n]
#                     flag = dfs(alpha, i+1, used + [n], numlist + [n], cantzero)
#                     if flag:
#                         return True
#             return False

#         alpha = result
#         cantzero = [result[0]]
#         for w in words:
#             alpha += w
#             cantzero += [w[0]]
#         alpha = list(set(alpha))
#         cantzero = list(set(cantzero))
#         print(alpha) 
#         print(cantzero)
#         res = dfs(alpha, 0, [], [], cantzero)
#         return res


# class Solution(object):
    # def isSolvable(self, words, result):
    #     """
    #     :type words: List[str]
    #     :type result: str
    #     :rtype: bool
    #     """

    #     def reverse(s):
    #         ret = ""
    #         for i in range(len(s) - 1, -1, -1):
    #             ret += s[i]
    #         return ret

    #     data = [reverse(w) for w in words]
    #     data.append(reverse(result))
    #     print(data)
    #     n = len(data)
    #     m = len(result)
    #     s = {}
    #     a = set()

    #     def work(k, n, m, y):
    #         if k >= n * m:
    #             return y == 0
    #         if (k + 1) % n == 0:
    #             if data[k % n][k // n] in s:
    #                 if y % 10 == s[data[k % n][k // n]]:
    #                     return work(k + 1, n, m, y // 10)
    #                 else:
    #                     return False
    #             else:
    #                 if y % 10 not in a:
    #                     a.add(y % 10)
    #                     s[data[k % n][k // n]] = y % 10
    #                     if work(k + 1, n, m, y // 10):
    #                         return True
    #                     a.remove(y % 10)
    #                     del s[data[k % n][k // n]]
    #                 else:
    #                     return False
    #         elif k // n >= len(data[k % n]):
    #             return work(k + 1, n, m, y)
    #         elif data[k % n][k // n] in s:
    #             if k // n == len(data[k % n]) - 1 and s[data[k % n][k // n]] == 0:
    #                 return False
    #             return work(k + 1, n, m, y + s[data[k % n][k // n]])
    #         else:
    #             for i in range(10):
    #                 if k // n == len(data[k % n]) - 1 and i == 0:
    #                     continue
    #                 if i not in a:
    #                     s[data[k % n][k // n]] = i
    #                     a.add(i)
    #                     if work(k + 1, n, m, y + i):
    #                         return True
    #                     a.remove(i)
    #                     del s[data[k % n][k // n]]
    #         return False
    #     return work(0, n, m, 0)


class Solution:
    def isSolvable(self, words, result):
        letter_dict = dict()
        for word in words:
            cnt = 1
            for letter in word[::-1]:
                if letter not in letter_dict:
                    letter_dict[letter] = 0
                letter_dict[letter] += cnt
                cnt *= 10
        cnt = 1
        for letter in result[::-1]:
            if letter not in letter_dict:
                letter_dict[letter] = 0
            letter_dict[letter] -= cnt
            cnt *= 10
        print(letter_dict)
        arr = sorted(letter_dict.values(), key=lambda x: abs(x), reverse=True)
        print(arr)
        length = len(arr)
        flag_num = [True] * 10
        flag_res = [False]
        def dfs(i, s):
            if flag_res[0]:
                return
            if i == length:
                if s == 0:
                    flag_res[0] = True
                return
            # 剪枝
            # num = 10
            for num in range(10)[::-1]:
                if flag_num[num]:
                    break
            if num * sum([abs(arr[j]) for j in range(i, length)]) < abs(s):
                return

            for num in range(10):
                if not flag_num[num]:
                    continue
                flag_num[num] = False
                dfs(i + 1, s + arr[i] * num)
                flag_num[num] = True
        dfs(0, 0)
        return flag_res[0]

words = ["SEND", "MORE"]
result = "MONEY"
res = Solution().isSolvable(words, result)
print(res)

words = ["SIX", "SEVEN", "SEVEN"]
result = "TWENTY"
res = Solution().isSolvable(words, result)
print(res)

words = ["THIS", "IS", "TOO"]
result = "FUNNY"
res = Solution().isSolvable(words, result)
print(res)

words = ["LEET", "CODE"]
result = "POINT"
res = Solution().isSolvable(words, result)
print(res)
