class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False

        d1={}
        d2={}
        for ch in s:
            if d1.get(ch):
                d1[ch]+=1
            else:
                d1[ch]=1

        for ch in t:
            if d2.get(ch):
                d2[ch]+=1
            else:
                d2[ch]=1

        return d1==d2