# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head
        n = 1
        while fast != None:

            if (fast.next == None):
                return slow
            if (fast.next.next == None):
                return slow.next
            
            fast = fast.next.next
            slow = slow.next
            n +=2

        return head
