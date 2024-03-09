class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        p = q = 0

        while p < len(nums1) and q < len(nums2):
            if nums1[p] < nums2[q]:
                p += 1
            elif nums1[p] > nums2[q]:
                q += 1

            else: return nums1[p]

        return -1

