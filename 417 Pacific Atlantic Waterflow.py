class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # ok let me explore -> and when we reach a border region we check for only pacific and then only atlantic or we can do both in two arrays and then union them
        if not heights or not heights[0]:
            return []
        rows,cols = len(heights),len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i,j,visited,prev_height):
            if i<0 or j<0 or i>=rows or j>= cols:
                return
            if (i,j) in visited:
                return
            if heights[i][j] < prev_height:
                return
            visited.add((i,j))
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
        # Pacific: top row & left column
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])

        # Atlantic: bottom row & right column
        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # Intersection
        return list(pacific & atlantic)