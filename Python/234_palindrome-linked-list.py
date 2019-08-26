# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None:
            return True

        p = head
        # while p:
        #     print(p.val)
        #     p = p.next

        buff = []
        # buff.append(p.val)
        # p = p.next

        while p:
            buff.append(p.val)
            p = p.next
        
        print(buff)

        i, j = 0, len(buff)-1

        while i <= j :
            if buff[i] != buff[j]:
                return False
            else:
                i += 1
                j -= 1
        return True



head = p = ListNode(0)
# data = []
data = [1,1,1,2,1]
for i in data:
    p.next = ListNode(i)
    p = p.next
result = Solution().isPalindrome(head.next)        
print(result)