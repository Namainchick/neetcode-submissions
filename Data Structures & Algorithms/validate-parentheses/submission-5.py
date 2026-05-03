class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets ={

            ")" : "(",
           
            "]" : "[",

            "}" : "{",
        }

        for i in s:
            print(brackets.get(None,))
            if not stack:
                stack.append(i)

            elif stack[-1] == brackets.get(i):
                stack.pop()
            else:
                stack.append(i)
            print(stack)
        print(stack)
        return True if not stack else False


