class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = (((n * (n + 1)) / 2) ** 0.5)
        return int(x) if x.is_integer() else -1
        