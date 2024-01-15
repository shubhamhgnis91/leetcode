class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        winner = {}
        looser = {}
        res=[]

        for match in matches:
            
            if match[0] in winner : 
                winner[match[0]] += 1
            
            else:
                winner[match[0]] = 1

            
            if match[1] in looser :
                looser[match[1]] += 1

            else:
                looser[match[1]] = 1

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

