# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        
        p = list1
        count = 0
        while True:
            
            if count == a - 1:
                q = p

                while a <= b:
                    a += 1
                    p = p.next
                
                q.next = list2

                while list2.next is not None:
                    list2 = list2.next

                list2.next = p.next

                break

            count += 1
            p = p.next

        return list1

                