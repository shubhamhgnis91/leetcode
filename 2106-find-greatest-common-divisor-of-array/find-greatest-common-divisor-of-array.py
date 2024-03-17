class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        divisor = min(nums)
        dividend = max(nums)

        while True:
            
            remainder = dividend % divisor

            if remainder == 0:
                return divisor

            dividend = divisor
            divisor = remainder 
