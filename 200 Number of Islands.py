class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # what if we iterate through -> any that we find we run a left right up down algorithm -> eventually would be island
        # once done set all the 1s to a # or something to recognize we have visited so that it skips it on check
        islands = 0
        def dfs(i,j):
            if i>=len(grid) or i<0 or j>=len(grid[i]) or j<0:
                return
            if grid[i][j]=="1":
                grid[i][j]="#"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            else:
                return
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] =="1":
                    islands+=1
                    dfs(i,j)
        return islands