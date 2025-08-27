class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        m = {}

        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            m[seq] = m.get(seq, 0) + 1
        
        res = []

        for item in m:
            if m[item] > 1:
                res.append(item)
        
        return res