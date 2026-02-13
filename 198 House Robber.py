class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ok lets iterate through a list -> we just cant do like i+1 of the location
        n = len(nums) # so we found how many possible houses
        if n == 1:
            return nums[0] # edge case # we could also do n = 2 as well but yeah
        dp = [0] * n # create a list of length n with all 0
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1]) # is it more profitable to rob the first house or the second house
        for i in range(2,n):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]