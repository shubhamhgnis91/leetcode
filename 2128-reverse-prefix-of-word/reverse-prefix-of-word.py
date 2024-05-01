class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        index = -1
        
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break

        if index == -1:
            return word

        s = ""
        temp = index
        
        while index >= 0:
            
            s += word[index]
            index -= 1

        return s + word[temp + 1::]
        