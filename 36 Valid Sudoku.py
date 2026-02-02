class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set() # all the stuff we've seen
        for i in range(9):
            for j in range(9):
                v = board[i][j] # Variable at i,j
                if v != ".":
                    if ((i, v) in seen or # if at point ()
                        (v, j) in seen or
                        (i//3, j//3, v) in seen):
                        return False
                    seen.add((i, v))
                    seen.add((v, j))
                    seen.add((i//3, j//3, v))
        return True