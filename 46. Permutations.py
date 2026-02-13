class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # we want to do like left to right 
        # we want it to go from start at 1 -> then set the next value as i + j where j is the length -i

        ans = []
        
        def dfs(start): 
            if start == len(nums):
                ans.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start],nums[i] = nums[i],nums[start]
                dfs(start+1)
                nums[start],nums[i] = nums[i],nums[start]
        dfs(0)
        return ans

