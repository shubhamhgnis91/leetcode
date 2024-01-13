class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        d={}
        count=0

        for ch in s:
            if ch in d:
                d[ch] += 1

            else:
                d[ch] = 1
        
        for ch in t:
            if ch not in d or d[ch] == 0:
                count += 1

            else:
                d[ch] -= 1

        return count
            