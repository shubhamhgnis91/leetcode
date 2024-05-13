class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')
        words = words[::-1]

        res = ""

        for word in words:
            if word != '':
                res += word
                res += ' '

        return res[:-1]