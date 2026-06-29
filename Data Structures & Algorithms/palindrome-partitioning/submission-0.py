"""
brute force would be to build every substring and check each if they are a palindrome. For each split. 
Can we store information form previous string to find palindrome easier. 
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(index, current):
            if index == len(s):
                self.result.append(current.copy())
                return 
            
            for i in range(index, len(s)):
                sub = s[index: i+1]
                if is_palindrome(sub):
                    current.append(sub)
                    backtrack(i+1,current)
                    current.pop()
        
        backtrack(0,[])
        return self.result