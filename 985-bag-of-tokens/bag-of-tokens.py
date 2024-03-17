class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        
        tokens.sort()
        p = 0
        q = len(tokens) -1
        score = 0

        while p <= q:
            if power >= tokens[p]:
                power -= tokens[p]
                score += 1
                p += 1

            elif score and p != q:
                power += tokens[q]
                score -= 1
                q -= 1

            else:
                break

        return score