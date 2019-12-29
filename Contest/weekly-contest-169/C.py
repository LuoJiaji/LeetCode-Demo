class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        # print(len(arr), start)
        if 0 not in arr:
            return False
        curr = [start]
        tmp = []
        visited = [start]
        flag = True
        while flag:
            for i in curr:
                if arr[i] == 0:
                    return True
                p = i + arr[i]
                if 0 <= p < len(arr):
                    tmp += [p]
                p = i - arr[i]
                if 0 <= p < len(arr):
                    tmp += [p]
            tmp = list(set(tmp))
            # print(tmp)
            curr = tmp
            np = [i for i in tmp if i not in visited]
            if np == []:
                return False
            visited = list(set(visited + curr))
            tmp = []  
        # print(tmp)
    


arr = [4,2,3,0,3,1,2]
start = 5
res = Solution().canReach(arr, start)
print(res)

arr = [4,2,3,0,3,1,2]
start = 0
res = Solution().canReach(arr, start)
print(res)

arr = [3,0,2,1,2]
start = 2
res = Solution().canReach(arr, start)
print(res)

arr = [2,2,3,2,3]
start = 3
res = Solution().canReach(arr, start)
print(res)

arr = [58,48,64,36,19,19,67,13,32,2,59,50,29,68,50,0,69,31,54,20,22,43,30,9,68,71,20,22,48,74,2,65,27,54,30,5,66,24,64,68,9,31,50,59,15,72,6,49,11,71,12,61,5,66,30,1,2,39,59,35,53,21,76,17,71,40,68,57,64,53,70,21,50,49,25,63,35]
start = 46
res = Solution().canReach(arr, start)
print(res)