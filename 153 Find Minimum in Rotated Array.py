class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we will start with  a BST from the middle
        # Check Right of middle to see if is less (therefore is rotated)
        l,r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if (nums[m]>nums[r]):
                # Move right
                l = m+1
            else:
                # Move left
                r = m
        return nums[l]


        