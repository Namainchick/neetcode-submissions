class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets ={

            ")" : "(",
           
            "]" : "[",

            "}" : "{",
        }

        for i in s:
            if not stack:
                stack.append(i)
            elif stack[-1] == brackets.get(i):
                stack.pop()
            else:
                stack.append(i)
        return True if not stack else False


