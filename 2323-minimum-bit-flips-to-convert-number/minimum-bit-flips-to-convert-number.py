class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        res = start ^ goal

        return bin(res)[2:].count('1')