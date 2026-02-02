class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        minHeap = []
        for (num,freq) in freq.items():
            heapq.heappush(minHeap, (freq,num))
            if len(minHeap)>k:
                heapq.heappop(minHeap)
    
        result = []
        for (_, num) in minHeap:
            result.append(num)

        return result
