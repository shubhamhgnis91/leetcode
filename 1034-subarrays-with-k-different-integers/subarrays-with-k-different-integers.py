class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostDistinctK(nums, k):
            left = right = count = 0
            n = len(nums)

            freq = {}

            while right < n:
                
                freq[nums[right]] = freq.get(nums[right], 0) + 1

                while len(freq) > k:
                    freq[nums[left]] -= 1

                    if freq[nums[left]] == 0:
                        freq.pop(nums[left], None)

                    left += 1

                count += right - left + 1
                right += 1

            return count
            


        
        return atMostDistinctK(nums, k) - atMostDistinctK(nums, k - 1)