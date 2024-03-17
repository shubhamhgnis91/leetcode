class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        res = []

        for interval in intervals:
            if interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval

            elif interval[1] < newInterval[0]:
                res.append(interval)

            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        res.append(newInterval)
        return res