# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        header = p = head
        counter = 1
        while p.next:
            # print(p.val)
            p = p.next
            counter += 1
        p.next = header
        p = p.next
        step = counter - k%counter
        # print('counter:',counter)
        # print('step:', step)

        for i in range(step-1):
            # print(p.val)
            p = p.next
        # print(p.val)
        header = p.next
        p.next = None

        # p = header
        # while p:
        #     print(p.val)
        #     p = p.next
        
        return header


data = [1,2,3,4,5]
header = p = ListNode(0)
for i in data:
    p.next = ListNode(i)
    p = p.next
# p = header.next
# while p:
#     print(p.val)
#     p = p.next
k = 2
result = Solution().rotateRight(header.next, k)
p = result
while p:
    print(p.val)
    p = p.next


data = [0,1,2]
header = p = ListNode(0)
for i in data:
    p.next = ListNode(i)
    p = p.next
# p = header.next
# while p:
#     print(p.val)
#     p = p.next
k = 4
result = Solution().rotateRight(header.next, k)
p = result
while p:
    print(p.val)
    p = p.next