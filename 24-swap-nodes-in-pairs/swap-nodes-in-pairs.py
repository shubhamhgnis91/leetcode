# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        p = head
        q = head.next

        head = q

        while p and q:
            temp = q.next
            q.next = p
            p.next = temp

            if not temp or not temp.next:
                p.next = temp
                break

            p.next = temp.next
            p = temp
            q = p.next


            

        return head