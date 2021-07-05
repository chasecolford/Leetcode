class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # helper to convert board state to output format
        def convertBoard(state):
            board = []
            for row in state: board.append("".join(row))
            return board
        
        # the main backtracking function
        def backtrack(row, diagonals, antidiagonals, cols, state):
            
            # if row == n, we have found a valid board state
            if row == n:
                res.append(convertBoard(state))
                return
            
            # else, we have more rows and cols to check
            for col in range(n):
                
                # For each square on a given diagonal, the difference between the row and column indices (row - col) will be constant.
                # For each square on a given anti-diagonal, the sum of the row and column indexes (row + col) will be constant. 
                diag, antidiag = row - col, row + col
                
                # make sure we do not already have a queen placed that controls this location
                if (col in cols) or (diag in diagonals) or (antidiag in antidiagonals): continue
                
                # this is a valid location -> place the queen in this position
                cols.add(col)
                diagonals.add(diag)
                antidiagonals.add(antidiag)
                state[row][col] = "Q"
                
                # now process the next row by calling backtrack again with row + 1
                backtrack(row + 1, diagonals, antidiagonals, cols, state)
                
                # at this point, we have explored all possible valid paths with the queen
                # at this [row][col] position, so we need to remove the queen and 'backtrack'
                cols.remove(col)
                diagonals.remove(diag)
                antidiagonals.remove(antidiag)
                state[row][col] = "."
                
        res = []
        emptyBoard = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), emptyBoard)
        return res