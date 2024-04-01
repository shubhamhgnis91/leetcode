class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        right = len(s) - 1
        res = 0

        while s[right] == ' ':
            right -= 1

        while right >= 0 and s[right] != ' ':
            right -= 1
            res += 1

        return res