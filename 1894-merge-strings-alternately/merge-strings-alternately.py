class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        m = len(word1)
        n = len(word2)

        i, p, q = 0, 0, 0

        while p < m and q < n:
            if i % 2 == 0:
                res += word1[p]
                p += 1

            else:
                res += word2[q]
                q += 1

            i += 1

        if m > 0:
            res += word1[p:]
        
        if n > 0:
            res += word2[q:]

        return res
        