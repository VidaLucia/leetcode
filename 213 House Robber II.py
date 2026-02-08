class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0] # edge case
        if n == 2:
            return max(nums[0],nums[1])
        def rob(arr):
            prev2 = 0 # dp i-2 
            prev1 = 0 # dp i -1
            for x in arr:
                cur = max(prev1,prev2+x)
                prev2 = prev1
                prev1 = cur
            return prev1
        return max(
            rob(nums[:-1]),
            rob(nums[1:])
        )