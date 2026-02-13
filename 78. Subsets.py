class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        subset = []
        def create(i):
            if i ==len(nums):
                ans.append(subset[:])
                return
            subset.append(nums[i])
            create(i+1)
            subset.pop()
            create(i+1)
        create(0)
        return ans