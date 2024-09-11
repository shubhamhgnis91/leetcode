class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        val = bin(start ^ goal)
        count = val.count('1')

        return count