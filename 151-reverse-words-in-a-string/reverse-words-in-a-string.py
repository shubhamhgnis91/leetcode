class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')
        res = ""

        i = len(words) - 1

        while i >= 0:
            if words[i] != '':
                res += words[i] + ' '
            i -= 1

        return res[:-1]

