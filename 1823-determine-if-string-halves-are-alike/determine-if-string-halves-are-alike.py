class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        p=0
        q=len(s)/2

        count1=0
        count2=0

        while p!=len(s)/2:
            if s[p] == 'a' or s[p] == 'A' or s[p] == 'e' or s[p] == 'E' or s[p] == 'i' or s[p] == 'I' or s[p] == 'o' or s[p] == 'O' or s[p] == 'u' or s[p] == 'U' :
                count1+=1
            if s[q] == 'a' or s[q] == 'A' or s[q] == 'e' or s[q] == 'E' or s[q] == 'i' or s[q] == 'I' or s[q] == 'o' or s[q] == 'O' or s[q] == 'u' or s[q] == 'U' :
                count2+=1
            p+=1
            q+=1

        return count1==count2