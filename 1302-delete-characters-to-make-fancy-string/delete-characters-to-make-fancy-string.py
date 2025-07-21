class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        count=0
        prev=s[0]

        for char in s:
            if char==prev:
                count+=1
                if count<3:
                    res+=char

            elif char!=prev:
                count=1
                res+=char
                prev=char
                
        return res  

