# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        header = q = head
        new_data = p = ListNode(q.val)
        while q.next:
            # print(p.val, q.val)
            if p.val == q.next.val:
                q = q.next
            else:
                p.next = q.next
                p = p.next
        p.next = None
        
        # p = new_data
        # while p:
        #     print(p.val)
        #     p = p.next

        return new_data


tmp = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,5,6,6,6]
data = p = ListNode(0)
for i in tmp:
    p.next = ListNode(i)
    p = p.next

# p = data.next
# while p:W
#     print(p.val)
#     p = p.next

result = Solution().deleteDuplicates(data.next)

p = result
while p:
    print(p.val)
    p = p.next


result = Solution().deleteDsuplicates([])
print(result)
