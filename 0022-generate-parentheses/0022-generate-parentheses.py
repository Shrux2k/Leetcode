class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backTrack(opened, closed):
            
            if opened == closed == n:
                res.append("".join(stack))
                
            if opened < n:
                stack.append("(")
                backTrack(opened+1,closed)
                stack.pop()
            
            if closed < opened:
                stack.append(")")
                backTrack(opened,closed+1)
                stack.pop()
                
        backTrack(0,0)
        return res
                