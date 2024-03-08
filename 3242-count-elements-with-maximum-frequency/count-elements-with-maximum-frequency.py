class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        maxFreq = max(freq.values())
        count = 0

        for num in freq:
            if freq[num] == maxFreq:
                count += freq[num]

        return count