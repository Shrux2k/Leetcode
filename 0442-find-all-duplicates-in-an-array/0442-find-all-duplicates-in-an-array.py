from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c= Counter(nums)
        count = []
        for i in nums:
            if c[i]==2:
                if i not in count:
                    count.append(i)
        return count
    
    
    

                    
            