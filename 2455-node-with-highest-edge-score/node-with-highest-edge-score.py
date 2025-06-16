class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        revAdjList = collections.defaultdict(list)

        for i,j in enumerate(edges):
            revAdjList[j].append(i)

        maxScore = -1
        res = None
        
        for node in revAdjList:
            nodeScore = sum(revAdjList[node])

            if nodeScore > maxScore or (nodeScore == maxScore and node < res):
                res = node
                maxScore = nodeScore

        return res
