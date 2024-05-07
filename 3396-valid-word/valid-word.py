class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) < 3:
            return False

        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        vCount = 0
        cCount = 0

        for c in word:
            if not c.isalnum():
                return False

            if c.isalpha():
                if c in vowels:
                    vCount += 1

                else:
                    cCount += 1

        if vCount == 0 or cCount == 0:
            return False

        return True
