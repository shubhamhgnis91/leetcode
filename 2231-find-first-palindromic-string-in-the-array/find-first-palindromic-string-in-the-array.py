class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        def isPalindrome(word):
            n=len(word)

            for i in range(n/2):
                if word[i] != word[n-i-1]:
                    return False
            
            return True
        
        for word in words:
            if isPalindrome(word):
                return word
        
        return ""