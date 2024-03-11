class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        
        res = ""
        charMap = {}

        for letter in s:
            charMap[letter] = charMap.get(letter, 0) + 1

        print(charMap)

        for letter in order:
            if letter in charMap:
                while charMap[letter] > 0:
                        res += letter
                        charMap[letter] -= 1
                
        print(charMap)


        for letter in charMap:
            while charMap[letter] > 0:
                res += letter
                charMap[letter] -= 1
        
        print(charMap)
    
        return res

        