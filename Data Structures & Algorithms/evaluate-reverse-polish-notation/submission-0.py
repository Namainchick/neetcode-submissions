class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0 
        stack = []

        for i in tokens:
            if i == "+":
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif i == "-":
                result = stack.pop() - stack.pop()
                stack.append(result)
            elif i == "*":
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif i == "/":
                result = stack.pop() // stack.pop()
                stack.append(result)
            else:   
                stack.append(int(i))
        return result