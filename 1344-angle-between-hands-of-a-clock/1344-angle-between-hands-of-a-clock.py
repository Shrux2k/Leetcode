class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_hour = (hour * 30) + (0.5*minutes)
        angle_minute = minutes * 6
        
        angle_diff = abs(angle_hour - angle_minute)
        return min(angle_diff,360-angle_diff)
        
    
        
    