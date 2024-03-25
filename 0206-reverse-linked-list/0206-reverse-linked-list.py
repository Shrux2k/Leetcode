# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return
        
        q = deque()
        node = head
        while node:
            q.append(node)
            node = node.next
        
        head = q.pop()
        current = head
        while q:
            temp = q.pop()
            current.next = temp
            current = current.next
        current.next = None
    
        return head
        
            
            
        
        