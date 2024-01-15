class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        winner = {}
        looser = {}
        res=[]

        for i in range(len(matches)):
            
            if matches[i][0] in winner : 
                winner[matches[i][0]] += 1
            
            else:
                winner[matches[i][0]] = 1

            
            if matches[i][1] in looser :
                looser[matches[i][1]] += 1

            else:
                looser[matches[i][1]] = 1

        row = []
        for player in winner : 
            if player not in looser :
                row.append(player)

        row.sort()
        res.append(row)

        row = []
        for player in looser : 
            if looser[player] == 1:
                row.append(player)

        row.sort()
        res.append(row)

        return res

