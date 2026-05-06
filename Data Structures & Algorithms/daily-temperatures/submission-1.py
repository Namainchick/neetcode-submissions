class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                sol[j] = i-j
            stack.append(i)
        return sol
#idee hat gefehlt das befreien war die idee. ohne zu wissen dass es eine stack aufgabe wäre hätte ich es nie gewusst plus ich dachte erstmal an ddouble stack denn es muss beim einfügen info gespeichert werden die danach helfen kann 