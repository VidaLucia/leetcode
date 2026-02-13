class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        top = [1]*n
        for _ in range(m-1):
            currentRow = [1]*n
            for i in range(1,n):
                currentRow[i]=currentRow[i-1]+top[i]
            top = currentRow
        return top[-1]
        