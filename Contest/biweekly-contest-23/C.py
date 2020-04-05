class Solution(object):
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        """
        :type radius: int
        :type x_center: int
        :type y_center: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        if x1 <= x_center <= x2:
            if y1 - radius <= y_center and y2 + radius >= y_center:
                return True
            else:
                return False
        elif y1 <= y_center <= y2:
            if x1 - radius <= x_center and x2 + radius >= x_center:
                return True
            else:
                return False
        else:
            x = min( abs(x_center - x1), abs(x_center - x2))
            y = min( abs(y_center - y1), abs(y_center - y2))
            if x**2 + y**2 <= radius**2:
                return True
            else:
                return False

            
         
        


radius = 1
x_center = 0
y_center = 0
x1 = 1
y1 = -1
x2 = 3
y2 = 1
res = Solution().checkOverlap(radius, x_center, y_center, x1, y1, x2, y2)
print(res)

radius = 1
x_center = 0
y_center = 0
x1 = -1
y1 = 0
x2 = 0
y2 = 1
res = Solution().checkOverlap(radius, x_center, y_center, x1, y1, x2, y2)
print(res)

radius = 1
x_center = 1
y_center = 1
x1 = 1
y1 = -3
x2 = 2
y2 = -1
res = Solution().checkOverlap(radius, x_center, y_center, x1, y1, x2, y2)
print(res)