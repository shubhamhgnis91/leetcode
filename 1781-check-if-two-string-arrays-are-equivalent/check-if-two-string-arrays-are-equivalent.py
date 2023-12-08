class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w1=""
        w2=""
        for i in range(len(word1)):
            w1=w1+word1[i]

        for i in range(len(word2)):
            w2=w2+word2[i]

        return True if w1==w2 else False