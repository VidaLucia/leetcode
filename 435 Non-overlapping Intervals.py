class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # what if i make a set of values -> each one can only appear twice max for non overlapping -> unless 
        ans = 0
        intervals.sort(key=lambda x:x[1]) # sorting by the 2nd balue
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            if prev_end > intervals[i][0]:
                ans+=1
            else:
                prev_end = intervals[i][1]
        return ans