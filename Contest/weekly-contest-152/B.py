class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(calories):
            if i + k > len(calories):
                break
            tmp = calories[i:i+k]
            # print(tmp)
            i += 1
            if sum(tmp) > upper:
                res += 1
            elif sum(tmp) < lower:
                res -= 1

        # print('res:', res)
        return res

    

calories = [1,2,3,4,5]
k = 1
lower = 3
upper = 3
result = Solution().dietPlanPerformance(calories, k, lower, upper)
print(result)

calories = [3,2]
k = 2
lower = 0
upper = 1
result = Solution().dietPlanPerformance(calories, k, lower, upper)
print(result)

calories = [6,5,0,0]
k = 2
lower = 1
upper = 5
result = Solution().dietPlanPerformance(calories, k, lower, upper)
print(result)

calories = [6,13,8,7,10,1,12,11]
k = 6
lower = 5
upper = 37
result = Solution().dietPlanPerformance(calories, k, lower, upper)
print(result)
