# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        mp = {}
        dummy = ListNode(0)
        dummy.next = head

        cSum = 0
        p = dummy

        while p:
            cSum += p.val
            mp[cSum] = p
            p = p.next
        
        cSum = 0
        p = dummy

        while p:
            cSum += p.val
            p.next = mp[cSum].next
            p = p.next

        return dummy.next
