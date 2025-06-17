class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        left = 0
        result = 0
        
        for right in range(n):
            # If s[right] is duplicate in current window, move left until it's removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            # Update max length
            result = max(result, right - left + 1)
        
        return result
