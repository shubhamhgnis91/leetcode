class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = []
        freq1 = {}
        

        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1        
        
        for num in nums2:
            if num in freq1 and freq1[num] > 0:
                res.append(num)
                freq1[num] -= 1

        return res
        