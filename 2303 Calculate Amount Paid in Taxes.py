class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        # we should start from reverse
        temp = 0
        ans = 0.0
        for bracket in brackets:
            if income <= temp:
                break
            taxable = min(income,bracket[0])-temp
            ans+=taxable * bracket[1]/100.0
            temp = bracket[0]
        return ans

