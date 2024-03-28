class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        
        for i in nums:
            if i in visited:
                return True
            else:
                visited.add(i)
        
        return False
        