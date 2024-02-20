class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = {}

        for num in nums:
            numbers[num] = numbers.get(num,0) + 1
        
        for num in numbers:
            if numbers[num] == 1:
                return num