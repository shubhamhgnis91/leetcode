# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next

        while curr:
            p = curr.next
            curr.next = prev
            prev = curr
            curr = p
        
        slow.next = None

        head1 = head
        head2 = prev

        while head2:
            p = head1.next
            head1.next = head2
            head1 = head2
            head2 = p
        


