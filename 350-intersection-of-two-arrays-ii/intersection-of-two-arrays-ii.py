class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = []
        freq1 = {}
        freq2 = {}

        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1        
        
        for num in nums2:
            freq2[num] = freq2.get(num, 0) + 1

        
        if len(freq1) > len(freq2):
            freq1, freq2 = freq2, freq1

        for num in freq1:
            count = 0
            if num in freq2:
                count = min(freq1[num], freq2[num])

                while count > 0:
                    res.append(num)
                    count -= 1
        
        return res

 
        