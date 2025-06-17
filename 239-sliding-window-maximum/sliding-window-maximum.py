class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # index
        res = []
        l = 0
        r = 0

        while r < len(nums):

            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # remove left value from window
            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1

        return res