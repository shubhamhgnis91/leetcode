class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[1])
        res = 0
        arrow = 0

        for point in points:
            if point[0] > arrow or res == 0:
                res += 1
                arrow = point[1]

        return res