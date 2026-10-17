class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(i,j):
            if i>= 0 and j<n and s[i] == s[j]:
                return expand(i-1,j+1)
            return i+1,j-1

        result_i,result_j = 0,0

        for i in range(n-1):
            i1,j1 = expand(i,i)
            i2,j2 = expand(i,i+1)

            if result_j - result_i < j1 - i1:
                result_i,result_j = i1,j1

            if result_j - result_i < j2 - i2:
                result_i,result_j = i2,j2
            
        return s[result_i:result_j+1]