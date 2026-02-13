class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # ok what i was thinking was
        # we have a lowest coins counter 
        # then we iterate through that list
        # try and add as many of the largest first then the next largest 

        array = [amount+1]*(amount+1)
        array[0] = 0
        for i in range(1,amount+1): # amount of coins
            for c in coins:
                if i-c >=0:
                    array[i]=min(array[i],1+array[i-c])
        return array[-1] if array[-1] != amount +1 else -1