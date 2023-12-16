class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False

        
        for ch in s:
            if s.count(ch)!=t.count(ch):
                return False
        
        return True