class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        substrings = set(s[i:i + 2] for i in range(len(s) - 1))
        
        s = s[::-1]
        
        for i in range(len(s) - 1):
            if s[i:i+2] in substrings:
                return True
            
        return False