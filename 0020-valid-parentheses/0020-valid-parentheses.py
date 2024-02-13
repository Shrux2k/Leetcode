class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        map = {')':'(','}':'{',']':'['}
        
        for char in s:
            if char in map.values():
                Stack.append(char)
            elif char in map.keys():
                if not Stack or map[char]!=Stack.pop():
                    return False
        if Stack:
            return False
        else:
            return True
        
        