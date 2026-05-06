class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0 
        stack = []
        if len(tokens) == 1:
            return tokens[0]
        for i in tokens:
            print(stack,result)
            if i == "+":
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif i == "-":
                a = stack.pop()
                result = stack.pop() - a
                stack.append(result)
            elif i == "*":
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif i == "/":
                a = stack.pop()
                result = int(stack.pop() / a)
                stack.append(result)
            else:   
                stack.append(int(i))
        return result