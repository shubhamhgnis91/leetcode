class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        if len(trust) == 0:
            if n == 1:
                return 1
                
            return -1

        trustFreq = {}
        trustSomeone = {}

        for i in range(len(trust)):
            trustFreq[trust[i][1]] = trustFreq.get(trust[i][1], 0) + 1
            trustSomeone[trust[i][0]] = True            

        maxTrusted = max(trustFreq.items(), key = lambda x: x[1])
        
        if maxTrusted[0] not in trustSomeone and maxTrusted[1] == n - 1:
            return maxTrusted[0]

        return -1 
