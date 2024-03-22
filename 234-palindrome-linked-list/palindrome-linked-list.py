class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head
        rev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = rev
            rev = slow
            slow = slow.next
            rev.next = temp

        if fast:
            slow = slow.next

        while rev:
            if rev.val != slow.val:
                return False

            slow = slow.next
            rev = rev.next
        
        return True
