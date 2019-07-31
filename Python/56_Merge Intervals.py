class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return []

        intervals.sort(key = lambda x:x[0])
        new_data = []
        new_data.append(intervals[0])
        # print(new_data)
        j = 0
        for i in range(1,len(intervals)):
            if new_data[j][1] >= intervals[i][0] and new_data[j][1] <= intervals[i][1] and new_data[j][0] <= intervals[i][0]:
                new_data[j][1] = intervals[i][1]
                # print('1')
            
            elif new_data[j][0] <= intervals[i][0] and new_data[j][1] >= intervals[i][1]:
                # print('2')
                pass

            elif new_data[j][0] <= intervals[i][1] and new_data[j][0] >= intervals[i][0] and new_data[j][1] >= intervals[i][1]:
                # print('3')
                new_data[j][0] = intervals[i][0]
            
            elif new_data[j][0] >= intervals[i][0] and new_data[j][1] <= intervals[i][1]:
                # print('4')
                new_data[j][0] = intervals[i][0]
                new_data[j][1] = intervals[i][1]

            else:
                new_data.append(intervals[i])
                j += 1
                
        # print(new_data)
        return new_data

data = [[1,3],[2,6],[8,10],[15,18]]
result = Solution().merge(data)
print(result)

data = [[1,4],[4,5]]
result = Solution().merge(data)
print(result)

data = [[1,4]]
result = Solution().merge(data)
print(result)

data = [[1,4],[0,4]]
result = Solution().merge(data)
print(result)

data = [[1,4],[0,5]]
result = Solution().merge(data)
print(result)

data = [[2,3],[4,5],[6,7],[8,9],[1,10]]
# data.sort(key = lambda x:x[0])
# print(data)
result = Solution().merge(data)
print(result)
