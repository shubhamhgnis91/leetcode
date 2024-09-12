class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        m = {}
        for c in allowed:
            m[c] = m.get(c, 0) + 1

        res = 0
        
        for word in words:
            consistent = True
            for c in word:
                if c not in m:
                    consistent = False
                    break
            
            if consistent == True:
                res += 1

        return res
