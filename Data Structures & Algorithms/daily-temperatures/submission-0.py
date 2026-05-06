class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            print(stack)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                sol[j] = i-j
            stack.append(i)
        return sol
