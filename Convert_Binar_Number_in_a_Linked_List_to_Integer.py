# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        curr = head
        sum = 0;
        powerOf2 = 0;
        n = 0
        while curr!= None:
            n+=1
            curr = curr.next

        powerOf2 = n-1
        curr = head
        while curr != None:
            sum+=(curr.val)*(2**powerOf2)

            powerOf2-=1
            curr = curr.next
        return sum

