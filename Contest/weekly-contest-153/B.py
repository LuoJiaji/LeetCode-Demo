class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        w = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        c = int(year/100)
        year = year % 100
        # print(c)
        if month == 1 or month == 2:
            month += 12
            year -= 1
        week =  (year + int(year/4) + int(c/4) - 2 * c + int(26 * (month + 1)/10) + day - 1) % 7
        # print(w[week])
        return w[week]
        
day = 31
month = 8
year = 2019
result = Solution().dayOfTheWeek(day, month, year)
print(result)

day = 18 
month = 7 
year = 1999
result = Solution().dayOfTheWeek(day, month, year)
print(result)

day = 15
month = 8
year = 1993
result = Solution().dayOfTheWeek(day, month, year)
print(result)
