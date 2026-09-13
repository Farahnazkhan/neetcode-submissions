class Solution:
    def isDuplicate(self, array: List) -> bool:
        compare = set()
        for item in array:
            if item != '.' and item in compare:
                return True
            compare.add(item)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check for rows
        for row in board:
            if self.isDuplicate(row):
                return False
        
        #check for columns
        for i in range(9):
            col = [row[i] for row in board]
            if self.isDuplicate(col):
                return False
        
        #check for squares
        squares = [
            [board[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
            for i in range(0, 9, 3)
            for j in range(0, 9, 3)
        ]
        for square in squares:
            if self.isDuplicate(square):
                return False
        return True
        
