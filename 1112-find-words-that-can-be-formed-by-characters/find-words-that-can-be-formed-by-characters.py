class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        
        res = 0

        for word in words:
          good = True

          for c in word:
            if word.count(c) > chars.count(c):
              good = False
              break
          
          if good:
            res+=len(word)
            
        return res