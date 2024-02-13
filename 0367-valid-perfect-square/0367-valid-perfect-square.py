class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = 1
        b = 1
        while a*b != num:
            if a*b>num:
                return False
            else:
                a+=1
                b+=1
                
        return True
            
            