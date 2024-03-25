class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ''
        for i in s:
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                str += i
                
        
        str = str.lower()        
        reversed_str = str[::-1]
        if str == reversed_str:
            return True
        else:
            return False
        