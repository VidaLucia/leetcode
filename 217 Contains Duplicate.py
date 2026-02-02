class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dictnum = {}
        for i in nums:
            if i not in dictnum:
                dictnum[i]=1
            else:
                return True      
        return False