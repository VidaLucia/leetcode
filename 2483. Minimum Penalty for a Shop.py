class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        # String of customers

        # what if we combine the Ys together and Ns together
        # keep moving right until we get a negative -> 
        score = 0
        max_score = 0
        best_hour = 0
        for i in range(len(customers)):
            if customers[i]=="Y":
                score+=1
            else:
                score-=1
            if score > max_score:
                max_score = score
                best_hour = i+1
        return best_hour
