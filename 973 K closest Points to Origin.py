class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # notes to self -> just make a heapq sorted by (a)[b,c] where its only sorted by a for size
        heapAns = []
        
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heapAns, (-dist, point))
            if len(heapAns)> k:
                heapq.heappop(heapAns)
        ans = []
        for d,p in heapAns:
            ans.append(p)
        return ans