# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # p = head
        # while p:
        #     print(p.val)
        #     p = p.next
    
        p = None
        q = head     
  
        # p.next = None
        while q:
            # print(p.val, q.val)
            tmp = q
            q = q.next
            tmp.next = p
            p = tmp

        head = p

        return head

        # p = head
        # while p:
        #     print(p.val)
        #     p = p.next


class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # p = head
        # while p:
        #     print(p.val)
        #     p = p.next
    
        p = None
        q = head     
        # p.next = None
        while q:
            # print(p.val, q.val)
            q.next, p, q = p, q, q.next 
        head = p

        return head

        # p = head
        # while p:
        #     print(p.val)
        #     p = p.next
    
head = p = ListNode(0)
# data = []
data = [1,2,3,4,5,6,7,8,9]
for i in data:
    p.next = ListNode(i)
    p = p.next
result = Solution2().reverseList(head.next)

p = result
while p:
    print(p.val)
    p = p.next

