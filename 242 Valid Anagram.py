class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicts = {}
        dictt = {}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in dicts:
                    dicts[s[i]]=1
                else:
                    dicts[s[i]]+=1
                if t[i] not in dictt:
                    dictt[t[i]]=1
                else:
                    dictt[t[i]]+=1
        return dicts==dictt

                


        