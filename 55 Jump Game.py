class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums)-1 # end 
        for i in range(len(nums)-2,-1,-1):  # go from the 2nd end to the front
            if i + nums[i]>= goal:
                goal = i
        return True if goal == 0 else False
        