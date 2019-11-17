class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        R1 = [region1]
        while 1:
            for i in regions:
                if region1 in i[1:]:
                    R1.append(i[0])
                    break
            if R1[-1] == region1:
                break
            region1 = R1[-1]
        
        R2 = [region2]
        while 1:
            for i in regions:
                if region2 in i[1:]:
                    R2.append(i[0])
                    break
            if R2[-1] == region1:
                break
            region2 = R2[-1]

        # print(R1)
        # print(R2)
        ind1 = 0
        for i in range(len(R1)):
            if R1[i] in R2:
                ind1 = i
                break
        ind2 = 0
        for i in range(len(R2)):
            if R2[i] in R1:
                ind2 = i
                break
        # print(ind1, ind2)
        return R1[ind1]
            
            
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]]
region1 = "Quebec"
region2 = "New York"
res = Solution().findSmallestRegion(regions, region1, region2)
print(res)

regions = [["Earth", "North America", "South America"],
["North America", "United States", "Canada"],
["United States", "New York", "Boston"],
["Canada", "Ontario", "Quebec"],
["South America", "Brazil"]]
region1 = "Canada"
region2 = "South America"
res = Solution().findSmallestRegion(regions, region1, region2)
print(res)

regions = [["Earth", "North America", "South America"],
["North America", "United States", "Canada"],
["United States", "New York", "Boston"],
["Canada", "Ontario", "Quebec"],
["South America", "Brazil"]]
region1 = "Canada"
region2 = "Quebec"