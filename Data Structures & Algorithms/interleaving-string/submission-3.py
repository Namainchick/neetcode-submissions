from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        @cache
        def dfs(i,j,k):
            if k == n3:
                return i == n1 and j == n2 

            if i == n1:
                return s2[j:] == s3[k:]
            elif j == n2:
                return s1[i:] == s3[k:]
            elif s1[i] == s3[k] and s2[j] == s3[k]:
                return dfs(i+1,j,k+1) or dfs(i,j+1,k+1)
            elif s1[i] == s3[k]:
                return dfs(i+1,j,k+1)
            elif s2[j] == s3[k]:
                return dfs(i,j+1,k+1)
            else:
                return False


        return dfs(0,0,0)