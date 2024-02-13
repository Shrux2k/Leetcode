class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
    
        product = 1
        zero_count = 0
        index = float('-inf')
    
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
                if zero_count > 1:
                    ans = [0] * n
                    return ans
            
                index = i
                continue
        
            product *= nums[i]
    
        for i in range(n):
            if i == index:
                ans[i] = product
            elif index == float('-inf'):
                ans[i] = product // nums[i]
            else:
                ans[i] = 0
    
        return ans
        
        