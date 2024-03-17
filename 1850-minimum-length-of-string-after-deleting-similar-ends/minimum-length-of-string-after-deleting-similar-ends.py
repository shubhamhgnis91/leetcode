class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = 0
        q = len(s) - 1

        while p < q and s[p] == s[q]:
            ch = s[p]

            while p <= q and s[p] == ch:
                p += 1

            while q >= p and s[q] ==ch:
                q -= 1

        return q - p + 1