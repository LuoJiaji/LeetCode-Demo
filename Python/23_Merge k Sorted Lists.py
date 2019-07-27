# /*
#  * @Author: JJ Luo 
#  * @Date: 2019-07-27 13:51:35 
#  * @Last Modified by:   JJ Luo 
#  * @Last Modified time: 2019-07-27 13:51:35 
#  */


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None

        result = lists[0]
        for i in range(1,len(lists)):
            result = self.Merge2Lists(result,lists[i])

        # cur = result
        # while cur :
        #     print(cur.val)
        #     cur = cur.next
        
        return result
    
    def Merge2Lists(self, List1, List2):
        header=  cur = ListNode(0)

        # while List1 :
        #     print(List1.val)
        #     List1 = List1.next

        while List1 and List2:
            if List1.val <= List2.val:
                cur.next = List1
                cur = cur.next
                List1 = List1.next
            else:
                cur.next = List2
                cur = cur.next
                List2 = List2.next
        if List1 :
            cur.next = List1
        else:
            cur.next = List2

        # cur = header.next
        # while cur :
        #     print(cur.val)
        #     cur = cur.next

        return header.next

class Solution2(object):
    def mergeKLists(self, lists):

        if lists = []:
            reutrn None
        # 将所有链表保存在一个数组中，并且排序
        data = []
        for i in lists:
            while i:
                data.append(i.val)
                i = i.next
        data.sort()
        # print(data)
        
        Header = cur = ListNode(0)
        for i in data:
            cur.next = ListNode(i)
            cur = cur.next

        # cur = Header
        # while cur :
        #     print(cur.val)
        #     cur = cur.next
        return Header.next


data = []
data.append(ListNode(1))
data[0].next = ListNode(4)
data[0].next.next = ListNode(5)

data.append(ListNode(1))
data[1].next = ListNode(3)
data[1].next.next = ListNode(4)
data.append(ListNode(2))
data[2].next = ListNode(6)

# result = Solution1().mergeKLists(data)
# result = Solution1().mergeKLists([])

result = Solution2().mergeKLists(data)