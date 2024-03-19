class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1

        maxCpu = max(count.values())
        res = (maxCpu - 1) * (n + 1)

        for item in count:
            if count[item] == maxCpu:
                res += 1
        
        return max(len(tasks), res)