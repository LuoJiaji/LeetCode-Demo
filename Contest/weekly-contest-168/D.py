class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        curr_box = initialBoxes
        curr_key = []
        for i in curr_box:
            curr_key += keys[i]
        ans = 0

        while curr_box:
            b = curr_box[-1]
            del curr_box[-1]
            if  status[b] == 1 or b in curr_key:
                print(b)
                curr_box += containedBoxes[b]
                curr_key += keys[b]
                ans += candies[b]
        return ans    

status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]
res = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
print(res)

# status = [1,0,0,0,0,0]
# candies = [1,1,1,1,1,1]
# keys = [[1,2,3,4,5],[],[],[],[],[]]
# containedBoxes = [[1,2,3,4,5],[],[],[],[],[]]
# initialBoxes = [0]
# res = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
# print(res)

# status = [1,1,1]
# candies = [100,1,100]
# keys = [[],[0,2],[]]
# containedBoxes = [[],[],[]]
# initialBoxes = [1]
# res = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
# print(res)

# status = [1]
# candies = [100]
# keys = [[]]
# containedBoxes = [[]]
# initialBoxes = []
# res = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
# print(res)

# status = [1,1,1]
# candies = [2,3,2]
# keys = [[],[],[]]
# containedBoxes = [[],[],[]]
# initialBoxes = [2,1,0]
# res = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
# print(res)
