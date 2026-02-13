class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def backtrack(a,b,sum):
            if not sum:
                return True
            c= str(a+b)
            return sum.startswith(c) and backtrack(b,int(c),sum[len(c):])
        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                # Skip invalid numbers with leading zeros
                if (num[0] == '0' and i > 1) or (num[i] == '0' and j > i + 1):
                    continue

                if backtrack(int(num[:i]), int(num[i:j]), num[j:]):
                    return True

        return False
# TODO: ?!?!?!?!?