class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ans = 0
        def expand(s,l,r):
            val = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -=1
                r+=1
                val+=1
            return val
        for i in range(len(s)):
            ans += expand(s,i,i)
            ans+= expand(s,i,i+1)
        return ans