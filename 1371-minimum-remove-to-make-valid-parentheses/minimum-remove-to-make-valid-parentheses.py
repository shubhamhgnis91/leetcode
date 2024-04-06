class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        openCount = 0
        closedCount = s.count(')')

        res = ""

        for c in s:
            if c == '(':
                openCount += 1

                if closedCount > 0 :
                    res += c

                    closedCount -= 1
            
            elif c == ')':

                if openCount > 0:
                    res += c

                    openCount -= 1

                else:
                    closedCount -= 1

            else:
                res += c


        return res
