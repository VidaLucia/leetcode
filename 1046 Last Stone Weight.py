class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # lets make a min heap
        stone_col = []
        for stone in stones:
            heapq.heappush(stone_col,-stone)
            # This gets everything into a min heap
        while len(stone_col) > 1:
            stone1 = -heapq.heappop(stone_col)
            stone2 = -heapq.heappop(stone_col)
            if stone1==stone2:
                continue
            if stone1>stone2:
                heapq.heappush(stone_col,-(stone1-stone2))
            else:
                heapq.heappush(stone_col,-(stone2-stone1))
        return -stone_col[0] if stone_col else 0
            

