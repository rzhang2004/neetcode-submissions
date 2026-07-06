class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkGroup(group):
            f = set()
            for tile in group:
                if tile in f:
                    return False
                elif tile != '.':
                    f.add(tile)
            return True

        # check rows
        rows = [x for x in board]
        for row in rows:
            if not checkGroup(row):
                return False

        # check cols
        for i in range(9):
            col = [x[i] for x in board]
            if not checkGroup(col):
                return False

        # check squares
        for top_y in range(0, 9, 3):
            for left_x in range(0, 9, 3):
                square = board[top_y][left_x:left_x+3] + board[top_y + 1][left_x:left_x+3] + board[top_y + 2][left_x:left_x+3]
                if not checkGroup(square):
                    return False
        
        return True




