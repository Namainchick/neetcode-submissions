class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.result = 0

        def check(i,j):
            if i>=0 and j<n and s[i] == s[j]:
                self.result += 1
                check(i-1,j+1)

        for i in range(n):
            check(i,i)
            check(i,i+1)

        return self.result 
