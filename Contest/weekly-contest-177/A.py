from datetime import date

class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        a1, b1, c1 = map(int, date1.split('-'))
        a2, b2, c2 = map(int, date2.split('-'))

        d1 = date(a1, b1, c1)
        d2 = date(a2, b2, c2)
        print(d1, d2)
        print(d1-d2)
        return abs((d1-d2).days)
        

date1 = "2019-06-29"
date2 = "2019-06-30"
res = Solution().daysBetweenDates(date1, date2)
print(res)

date1 = "2020-01-15"
date2 = "2019-12-31"
res = Solution().daysBetweenDates(date1, date2)
print(res)