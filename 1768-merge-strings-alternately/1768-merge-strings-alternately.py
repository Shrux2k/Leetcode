class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        m, n = len(word1), len(word2)
        diff = abs(m - n)

        if m > n:
            word2 += ' ' * diff  
        elif n > m:
            word1 += ' ' * diff  

        for char1, char2 in zip(word1, word2):
            merged += char1 + char2

        return merged.replace(' ', '')  


                