class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = set(A)
        max_val = 0
        for i in A:
            max_val |= i
        print('max', max_val)
        ans.add(max_val)
        for i in range(len(A)):
            curr = 0
            j = i
            # while j < len(A) and curr < max_val:
            for j in range(i, len(A)):
                curr |= A[j]
                # print(i,j,curr,A[j])
                ans.add(curr)
                if curr >= max_val:
                    continue
                print(i,j,curr)
                # j += 1
        # print(ans)
        return len(ans)

data = [0]
res = Solution().subarrayBitwiseORs(data)
print(res)

data = [1,1,2]
res = Solution().subarrayBitwiseORs(data)
print(res)

data = [1,2,4]
res = Solution().subarrayBitwiseORs(data)
print(res)

data = [10,12]
res = Solution().subarrayBitwiseORs(data)
print(res)