class Solution:
    def isValid(self, s: str) -> bool:
        
        Stack = []
        map = {')':'(','}':'{',']':'['}
        
        for i in s:
            if i in map.values():
                Stack.append(i)
            elif i in map.keys():
                if not Stack or map[i]!=Stack.pop():
                    return False
        
        if Stack:
            return False
        else:
            return True
        
        
        
        
        
        
        
        
        