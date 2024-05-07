# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        head = prev

        p = head
        carry = 0
        while p is not None:
            
            num = (p.val) * 2 + carry
            carry = int(num / 10)
            digit = num % 10

            p.val = digit

            if p.next is None:
                q = p

            p = p.next

        if carry > 0:
            newNode = ListNode(carry)
            q.next = newNode

        prev = None
        current = head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        head = prev

        return head
        