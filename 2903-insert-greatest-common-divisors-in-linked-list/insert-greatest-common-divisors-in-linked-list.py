# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:        

        if not head or not head.next:
            return head

        p = head
        q = head.next

        while q is not None:
            a = p.val
            b = q.val

            g = math.gcd(a, b)

            newNode = ListNode(g)
            newNode.next = q
            p.next = newNode

            p = q
            q = q.next
        

        return head