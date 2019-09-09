class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        
        l = sum(distance)
        # print(l)

        if start > destination:
            start, destination = destination, start
        
        c = sum(distance[start: destination])
        rc = l - c
        # print(c, rc)

        return min(c, rc)


distance = [1,2,3,4]
start = 0
destination = 1
result = Solution().distanceBetweenBusStops(distance, start, destination)
print(result)

distance = [1,2,3,4]
start = 0
destination = 2
result = Solution().distanceBetweenBusStops(distance, start, destination)
print(result)

distance = [1,2,3,4]
start = 0
destination = 3
result = Solution().distanceBetweenBusStops(distance, start, destination)
print(result)