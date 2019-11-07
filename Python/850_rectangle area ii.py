class Solution:
    def rectangleArea(self, rectangles):
        """
        假设本题目中每一个线段是用元组表示的，且元组中只有两个元素，第一个小于第二个。
        :param rectangles:
        :return:
        """

        def get_div_lines(rectangles):
            """
            输入矩形列表，取出所有矩形的上下边界组成新列表，去除重复值，返回排序后的分隔线的y坐标列表。
            :param rectangles:
            :return:
            """
            return sorted(list(set([rect[1] for rect in rectangles] + [rect[3] for rect in rectangles])))

        def init_range_dict(div_lines):
            """
            根据边界划分整个坐标系，函数返回一个字典，字典中存储了每一个y轴区域上有覆盖的矩形的x范围，可能有多个x范围
            1. 字典的键key是各个y轴的分段，每个分段用元组合表示；
            2. 字典的值是线段列表，表示处在key范围内的所有x轴上的有覆盖的区域的x坐标范围，每条线段用元组表示
            函数返回该字典
            :param div_lines:
            :return:
            """
            return {(div_lines[i], div_lines[i+1]): [] for i in range(len(div_lines)-1)}

        def cut_rectangle(range_dict, div_lines, rectangle):
            """
            输入y轴分隔线，将当前矩阵用y轴分隔线切成不同小段，把切好的小矩形的x左右坐标放在range_dict中相应的位置，即加入到相应列表中。
            :param range_dict: 范围字典，每切一块矩阵都会进行分配和给更新键值
            :param div_lines: 分隔线们，或者每把刀所在位置，都是横线
            :param rectangle: 当前要被切的一个矩形，切好了放在字典中相应的位置
            :return:
            """
            x1, y1, x2, y2 = rectangle
            assert x1 < x2 and y1 < y2, 'Input Error, Please examine your input format.'
            for i in range(div_lines.index(y1), div_lines.index(y2)):
                range_dict[(div_lines[i], div_lines[i+1])].append((x1, x2))
            return range_dict

        def cut_rectangles(range_dict, div_lines, rectangles):
            """
            把所有矩形都进行切块和分配
            :param range_dict:
            :param div_lines:
            :param rectangles:
            :return:
            """
            for rect in rectangles:
                range_dict = cut_rectangle(range_dict, div_lines, rect)
            return range_dict

        def combine_line_segmentes(seg_list):
            """
            x方向上很多线段，这些线段可能重合，可以归并，例如[[1,3], [2,6], [7,9]]就可以归并为[[1, 6], [7, 9]
            :param seg_list: 输入切好的x轴线段们，进行一个整理和归并
            :return: 
            """
            if len(seg_list) <= 1:
                return seg_list
            # sorted_list = [tp[1] for tp in sorted(zip([seg[0] for seg in seg_list], seg_list))]
            seg_list.sort()
            sorted_list = seg_list
            new_list = []
            new_line_x1, new_line_x2 = sorted_list[0]
            i = 1
            while True:
                x1, x2 = sorted_list[i]

                if new_line_x1 <= x1 <= new_line_x2:
                    new_line_x2 = max(new_line_x2, x2)

                elif x1 > new_line_x2:
                    new_list.append((new_line_x1, new_line_x2))
                    new_line_x1, new_line_x2 = x1, x2

                if i == len(seg_list) - 1:
                    new_list.append((new_line_x1, new_line_x2))
                    break
                i += 1

            return new_list

        def calculate_area(range_dict):
            """
            整体计算
            :param range_dict: 
            :return: 
            """
            area = 0                                                    # 初始化面积
            for y_range, x_ranges in range_dict.items():                # 依次取出来字典中的键和值
                y_len = y_range[1] - y_range[0]                         # 字典的键实际代表当前的横条带区域，相减得到条带宽
                x_ranges = combine_line_segmentes(x_ranges)             # 字典的值是个x方向的线段列表，进行一下整理和归并
                x_len = sum([line[1]-line[0] for line in x_ranges])     # 计算x方向上的所有线段长度
                area += y_len * x_len                                   # 横纵方向上相乘即可得到落在当前横条带中小矩形的面积
            return area

        y_div_lines = get_div_lines(rectangles)                         # 获得每一把刀的位置
        range_dict = init_range_dict(y_div_lines)                       # 初始化菜篮子
        range_dict = cut_rectangles(range_dict, y_div_lines, rectangles)# 切菜，把每个矩形切好放在菜篮子覆中该放的位置
        area = calculate_area(range_dict)                               # 计算总的面积
        if area > 1000000007:                                           # 越界评判
            return area % 1000000007
        return area

data = [[0,0,2,2], [1,0,2,3], [1,0,3,1]]
res = Solution().rectangleArea(data)
print(res)

data = [[0,0,1000000000,1000000000]]
res = Solution().rectangleArea(data)
print(res)
