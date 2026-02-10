class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0]*(n+1)
        sub =1
        for i in range(1,n+1):
            # count how many 1s at each one in an array
            if sub * 2 ==i:
                sub =i
            dp[i]= dp[i-sub]+1
        return dp