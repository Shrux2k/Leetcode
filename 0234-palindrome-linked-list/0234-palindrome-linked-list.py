# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        q = deque()
        first, last = 0, 0
        
        while curr:
            q.append(curr.val)
            curr = curr.next
        
        while len(q) > 1:
            first = q.popleft()
            last = q.pop()
            if first != last:
                return False
        return True
                
        
        
        