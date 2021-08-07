class Solution:
    def checkMove(self, board: List[List[str]], rmove: int, cmove: int, color: str) -> bool:
        """
        we will just check all dirs
        """
        # helpers
        def good(r, c):
            if r < 0 or r >= 8: return False
            if c < 0 or c >= 8: return False
            return True
            
        def valid(chunk):
            n = len(chunk)
            if n < 3: return False
            if chunk[0] != chunk[-1]: return False
            
            # check the middle of the chunk
            ends = chunk[0]
            target = chunk[1]
            
            if ends == '.' or target == '.': return False # free cells are invald
            if target == ends: return False # middle must be different than ends
            for i in range(2, n-1): 
                if chunk[i] != target: return False
            print(chunk)
            return True
                
        
        # set the board to this color
        board[rmove][cmove] = color 
        
        dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]] # clockwise starting from top
        for d in dirs:
            r, c = rmove, cmove
            chunk = []
            while good(r, c):
                chunk.append(board[r][c])
                if valid(chunk): return True
                
                # move in dir
                r += d[0]
                c += d[1]
        return False