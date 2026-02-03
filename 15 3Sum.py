class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)== 3: # Edge case array size 3
            sum = 0
            for val in nums:
                sum+=val
            if sum!=0:
                return[]
            return [nums]
        else:
            answer =[]
            nums.sort()
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                left = i+1
                right = len(nums)-1
                
                while (left < right):
                    s = nums[i]+nums[left]+nums[right]
                    if s< 0:
                        left+=1
                    elif s> 0:
                        right-=1
                    else:
                        answer.append([nums[i],nums[left],nums[right]])
                        while left < right and nums[right] ==nums[right-1]:
                            right-=1
                        while left < right and nums[left] == nums[left+1]:
                            left+=1
                        left+=1
                        right-=1
            return answer

# Need to check for duplicates moving forward when you want to filter duplicates
