# /*
#  * @Author: JJ Luo 
#  * @Date: 2019-07-28 15:52:15 
#  * @Last Modified by:   JJ Luo 
#  * @Last Modified time: 2019-07-28 15:52:15 
#  */


# 自己写的超时了......
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        max_height = max(height)
        cur = [0] * len(height)
        res = height
        # print(res)
        # print(cur)
        result = 0 
        for i in range(max_height):
            cur = [0] * len(height)
            for i in range(len(res)):
                if res[i]  > 0:
                    cur[i] = 1
                    res[i] -= 1
            # print(cur)

            flag_leaf = flag_right = 0
            flag = 0
            cout = 0
            cur_cout = 0
            for i in cur:
                if i == 1 and flag_leaf == 0:
                    flag_leaf = 1
                elif flag_leaf == 1 and i == 0:
                    cout += 1
                elif flag_leaf == 1 and i == 1:
                    cur_cout = cout
            result += cur_cout
        # print(result)
        return result


class Solution2:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        top = 0
        for i in range(len(A)):
            if A[top] < A[i]:
                top = i
        print(A)

        second_top = 0
        for i in range(top):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]
            print(second_top, i, A[second_top], A[i], A[second_top] - A[i])

        second_top = len(A) - 1
        for i in reversed(range(top, len(A))):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]
            print(second_top, i, A[second_top], A[i], A[second_top] - A[i])

        return result


# data = [0,1,0,2,1,0,1,3,2,1,2,1]
# result = Solution().trap(data)
# print(result)

# data = []
# result = Solution().trap(data)
# print(result)

data = [0,1,0,2,1,0,1,3,2,1,2,1]
result = Solution2().trap(data)
print(result)