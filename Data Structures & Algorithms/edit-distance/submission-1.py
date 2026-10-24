class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        idea: two pointers one for each word. if they are the same just move on. Why move on? If they have the same character it means this one is a valid part of word1 for the valid solution we are trying to build. if if they are not the same we have to try 3 things either add a character and add cost by one. and then move word 2 counter by one beacuase word1 pointer is still add the same character. or delete that character and add cost up and just move on with word1 pointer. and if replace we just move both ponters and also add the cost
        """
        n1 = len(word1)
        n2 = len(word2)


        dp = [[-1] * n2 for _ in range(n1)]

        def dfs(i,j):
            if i == n1:
                return n2 - j

            if j == n2:
                return n1 - i

            if dp[i][j] != -1:
                return dp[i][j]
            
            sol = 0
            if word1[i] == word2[j]:
                sol = dfs(i+1,j+1)
            else:
                sol = min(dfs(i,j+1),dfs(i+1,j),dfs(i+1,j+1)) + 1

            dp[i][j] = sol
            return sol

        return dfs(0,0)