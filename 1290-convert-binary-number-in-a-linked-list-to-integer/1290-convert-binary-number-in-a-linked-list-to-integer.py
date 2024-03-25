# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        num = 0
        while head:
            num = (num*10) + head.val
            head = head.next
        print(num)
        return self.binToNumber(str(num))
            
        
    def binToNumber(self, binary):
        
        power = 0
        total = 0
        for i in binary[::-1]:
            if i == '1':
                total = total + pow(2,power)
                print(total)
            power += 1
            
        return total
        
        
    
    
        
        
        