class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        score = 0

        for p in range(len(s)):
            appeared = set()
            currScore = 0
            
            for q in range(p, len(s)):
                if s[q] in appeared:
                    break
                appeared.add(s[q])
                currScore += 1
            
            score = max(score, currScore)
        
        return score