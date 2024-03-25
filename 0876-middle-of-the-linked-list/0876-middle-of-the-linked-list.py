# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
        if not head:
            return
        
        
        node = head
        count = 0
        while head:
            head = head.next
            count += 1
        
        
        num = int(count/2)
        if count % 2 == 0:
            
            for i in range(0, num):
                node = node.next
            return node
        else:
            for i in range(0, num):
                node = node.next
            return node
        
            
            
            
        
            
            
        
        
        
        