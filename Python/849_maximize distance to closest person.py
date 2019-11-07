class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        l = len(seats)
        left = [0] * l
        right = [0] * l
        
        if seats[0] == 0:
            left[0] = float('inf')
        else:
            left[0] = 0
        for i in range(1,l):
            if seats[i] == 1:
                left[i] = 0
            else:
                left[i] = left[i-1] + 1

        if seats[-1] == 0:
            right[-1] = float('inf')
        else:
            right[-1] = 0
        for i in reversed(range(0,l-1)):
            if seats[i] == 1:
                right[i] = 0
            else:
                right[i] = right[i + 1] + 1
        print(left)
        print(right)
        
        dis_min = []

        for i in range(0,l):
            if left[i] != 0 and right[i] != 0:
                dis_min.append(min(left[i], right[i]))



        print(dis_min)
        return max(dis_min)



data = [1,0,0,0,1,0,1]
res = Solution().maxDistToClosest(data)
print(res)

data = [1,0,0,0]
res = Solution().maxDistToClosest(data)
print(res)

data = [1,0,0]
res = Solution().maxDistToClosest(data)
print(res)

data = [0,1]
res = Solution().maxDistToClosest(data)
print(res)
