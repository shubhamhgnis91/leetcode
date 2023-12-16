class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        for i in range(len(s)):
            cmap={}
            count=1
            cmap[s[i]]=1
            for j in range(i+1,len(s)):
                if cmap.get(s[j]) is None:
                    cmap[s[j]]=1
                    count+=1
                else:
                    break
            max_len=max(max_len,count)
        return max_len