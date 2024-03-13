class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = (((n * (n + 1)) / 2) ** 0.5)
        if res.is_integer():
            return int(res)
        return -1
        