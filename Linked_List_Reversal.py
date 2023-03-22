# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        curr = head
        p = n = None
        while curr.next != None:
            n = curr.next
            curr.next = p
            p = curr
            curr = n

        head = curr
        head.next = p
        return head
