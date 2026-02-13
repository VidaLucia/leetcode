class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        # minute will always be constant location
        # hour is going to be location-1+1*% completion
        hour = hour % 12
        
        minute_angle = 6 * minutes
        hour_angle = 30 * hour + 0.5 * minutes
        
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
# Cheesed this shouldve been easier lol