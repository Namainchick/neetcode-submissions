class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []

        def backtrack(temp,open,close):
            if len(temp) == n*2:
                self.result.append("".join(temp))
                return 

            if open < n:
                temp.append("(")
                backtrack(temp,open+1,close)
                temp.pop()

            if open > close:
                temp.append(")")
                backtrack(temp,open,close+1)
                temp.pop()
        
        backtrack([],0,0)
        return self.result