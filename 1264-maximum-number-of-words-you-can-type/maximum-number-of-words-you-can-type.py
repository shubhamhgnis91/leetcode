class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        words = text.split()

        res = 0

        for word in words:
            for ch in word:
                if ch in brokenLetters:
                    res += 1
                    break
        
        return len(words) - res