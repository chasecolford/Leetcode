class Solution:
    def totalNQueens(self, n: int) -> int:

        # the main backtracking function
        def backtrack(row, diagonals, antidiagonals, cols):
            
            # if row == n, we have found a valid board state
            if row == n:
                self.res += 1
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
                
                # now process the next row by calling backtrack again with row + 1
                backtrack(row + 1, diagonals, antidiagonals, cols)
                
                # at this point, we have explored all possible valid paths with the queen
                # at this [row][col] position, so we need to remove the queen and 'backtrack'
                cols.remove(col)
                diagonals.remove(diag)
                antidiagonals.remove(antidiag)
                
        self.res = 0
        backtrack(0, set(), set(), set())
        return self.res