from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        """
        Main backtracking function
        """
        def backtrack(row, col):

            # handle wrapping and checking if we are done
            if col == 9:
                col = 0
                row += 1
            
            # if the row > 8, we have filled with a valid permuation, stop backtracking
            if row > 8: 
                self.done = True
                return
            
            # if this location is already a number, go to next location
            if board[row][col] != ".": return backtrack(row, col + 1)
            
            # calculate the id for the 3x3
            threesID = ((row // 3) * 3 + col // 3)
            
            # for each of the possible values
            for value in range(1, 10):
                
                # check if the this value is 
                valid = validate(value, row, col)
                    
                # if this was a valid value for the given board state
                if valid:
                    
                    # update the board state and sets
                    board[row][col] = str(value)
                    rows[row].add(value)
                    cols[col].add(value)
                    threes[threesID].add(value)
                    
                    # continue down this path
                    backtrack(row, col + 1)
                    if self.done: return
                    
                    # we have checked all paths, now remove this value
                    board[row][col] = "."
                    rows[row].remove(value)
                    cols[col].remove(value)
                    threes[threesID].remove(value)
                
                                 
        """
        Helper function that validates a given value choice based on current board state
        we can consider using sets to store the values that are in each of the sections
        """
        def validate(value, row, col):
            threesID = ((row // 3) * 3 + col // 3)
            if value in rows[row]: return False
            if value in cols[col]: return False
            if value in threes[threesID]: return False
            return True
        
        """
        Initializes the sets to hold all of the static starting values of the initial board state
        """
        def initializeSets():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".": continue
                    threesID = ((r // 3) * 3 + c // 3)
                    val = int(board[r][c])
                    rows[r].add(val)
                    cols[c].add(val)
                    threes[threesID].add(val)
            
        """
        Main Entry
        """
        self.done = False # lazy, stores if we still need to backtrack so we easily stop when don
        
        # trying sets of sets for the sections for make the validate function faster
        rows, cols, threes = defaultdict(set), defaultdict(set), defaultdict(set)
        
        # initialize the sets with the static values from the starting board
        initializeSets()
        
        # begin backtracking from the starting location
        backtrack(0, 0)
        
        """
        Do not return anything, modify board in-place instead.
        """
        return 