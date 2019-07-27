# /*
#  * @Author: JJ Luo 
#  * @Date: 2019-07-27 17:05:04 
#  * @Last Modified by:   JJ Luo 
#  * @Last Modified time: 2019-07-27 17:05:04 
#  */

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        data = []
        header = cur = head
        while cur:
            data.append(cur.val)
            cur = cur.next

        # print(data)

        for i in range(int(len(data)/k)):
            # print(data[i*k : (i+1)*k:])
            tmp = data[i*k : (i+1)*k:]
            data[i*k : (i+1)*k:] = tmp[::-1]
            # print(tmp)
        
        # print(data[(i+1)*k:])
        print(data)

        header = cur = ListNode(0)
        for i in data:
            # print(i)
            cur.next = ListNode(i)
            cur = cur.next
            # print(cur.val)
        
        # cur = header.next
        # while cur:
        #     print(cur.val)
        #     cur = cur.next
        return header.next


l = [1,2,3,4,5]
Headar = data = ListNode(0)
for i in l:
    data.next = ListNode(i)
    data = data.next
    # print(i)
data = Headar.next
result = Solution().reverseKGroup(data, 2)
while result:
    print(result.val)
    result = result.next

