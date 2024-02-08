class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words = s.split()
        if len(pattern) != len(words):
            return False

        m1 = {}
        m2 = {}

        for i in range(len(pattern)):
            ch = pattern[i] 
            word = words[i] 

            if ch not in m1:
                if word in m2:
                    return False
                
                m1[ch] = word
                m2[word] = ch
            
            else:
                if m1[ch] != word or m2[word] != ch:
                    return False           

        return True