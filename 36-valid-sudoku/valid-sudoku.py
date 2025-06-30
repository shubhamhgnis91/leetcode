class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validUnit(unit):
            s = set()

            for num in unit:
                if num != ".":
                    if num in s:
                        return False

                    s.add(num)

            return True

        for row in board:
            if not validUnit(row):
                return False

        
        for col in zip(*board):
            if not validUnit(col):
                return False

        for bi in (0, 3, 6):
            for bj in (0, 3, 6):
                block = [
                    board[r][c]
                    for r in range(bi, bi + 3)
                    for c in range(bj, bj + 3)
                ]

                if not validUnit(block):
                    return False

        return True