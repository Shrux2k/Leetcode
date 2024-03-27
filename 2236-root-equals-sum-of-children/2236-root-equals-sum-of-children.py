# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        res = []
        
        def inOrder(root):
            
            if not root:
                return
            
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
        inOrder(root)
        
        if res[0] + res[2] == res[1]:
            return True
        else:
            return False
        