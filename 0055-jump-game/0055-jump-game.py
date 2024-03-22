class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        #make a pointer and jump based on next index
        #if it lands on the last index then return true
        #if it lands way after the last index then return false
        #wherever it jumps holds a value 0 then return false 
        
        
      gas = 0
      for n in nums:
        if gas < 0:
            return False
        elif n > gas:
            gas = n
        gas -= 1
            
      return True
            
        
        