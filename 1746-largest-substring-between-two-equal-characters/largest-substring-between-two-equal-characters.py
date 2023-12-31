class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic={}
        mlen=-1

        for i in range(len(s)):

            if s[i] not in dic:
                dic[s[i]]=(i,i)
                
            else:
                first,_=dic[s[i]]
                last=i
                
                if last-first-1 > mlen:
                    mlen=last-first-1
                    dic[s[i]]=(first,last)

        return mlen