class Solution(object):
    def countBlackBlocks(self, m, n, coordinates):
        """
        :type m: int
        :type n: int
        :type coordinates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0]*5
        blockCount = defaultdict(int)

        for x,y in coordinates:
            for dx in (-1,0):
                for dy in (-1,0):
                    i = x+dx
                    j = y + dy
                    if 0 <=i < m-1 and 0<=j<n-1:
                        blockCount[(i,j)]+=1
        for count in blockCount.values():
            ans[count]+=1
        total_blocks=(m-1)*(n-1)
        ans[0] = total_blocks-sum(ans[1:])
        return ans