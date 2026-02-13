class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def divisible(num):
            for v in str(num):
                if int(v) ==0:
                    return False
                if num%int(v) != 0:
                    return False
            return True
        ans = []
        for i in range(left,right+1):
            if divisible(i):
                ans.append(i)
        return ans

        