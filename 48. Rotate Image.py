class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # what if we snake this
        # double flip
        edge = len(matrix)
        top = 0
        bot = edge-1

        while top<bot: # flip in half borger style
            for col in range(edge):
                temp = matrix[top][col]
                matrix[top][col]=matrix[bot][col]  
                matrix[bot][col]= temp
            top+=1
            bot -=1
        for row in range(edge): # flip through diagonal
            for col in range(row+1,edge):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row]= temp
        return matrix