class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        if len(strs)==1: # if there is only one thing
            return [strs]
        for word in strs:
            str_char = list(word) # should now be sorted alphabetically
            str_char.sort()
            str_char = "".join(str_char)
            if str_char not in group:
                group[str_char] = [word]
            else:
                group[str_char].append(word)

                # now should be like {["a","b"]:[ab,ba]}
        return [wordgroup for wordgroup in group.values()]
        

        
        