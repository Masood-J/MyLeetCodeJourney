# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
          return None



        current=head
        fast=head.next.next
        while fast and fast.next is not None:

            current=current.next
            fast=fast.next.next

        
        current.next=current.next.next
        return head

        