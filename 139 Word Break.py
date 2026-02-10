class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # so what im thinking right now is we start with a array where we iterate through so like 
        # c a t-> if that ever matches in the dict terminate there and move to the next starting point
        # if we reach the end and nothing changes we iterate at the next possible val?
        dp= [False]* (len(s)+1)
        dp[0] = True # first value of an string is null
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]