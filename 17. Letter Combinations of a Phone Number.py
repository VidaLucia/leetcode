class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        phone = {
            1: [],
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        def backtrack(idx,comb):
            if idx == len(digits):
                ans.append(comb[:])
                return
            for l in phone[int(digits[idx])]:
                backtrack(idx+1,comb+l)
        backtrack(0, "")    
        return ans