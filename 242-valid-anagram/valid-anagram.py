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

        for i in range(len(s)):
            if d1.get(s[i]):
                d1[s[i]]+=1
            else:
                d1[s[i]]=1

            if d2.get(t[i]):
                d2[t[i]]+=1
            else:
                d2[t[i]]=1

        return d1==d2