class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        brute force would be just to create all subsets and check if under of equal to amound everyhting over can be skipped

        better idea:
        best would be if we know how many different ways we got from cur to amount. 
        for that we would need to know how many ways there is to reach a specific amount. 
        for doubles we can just sort the array. How and what do we store? 
        just do the same as brute force but store the number of ways to a amount 
        """

        index = 0
        coins.sort()

        n = len(coins)
        dp = {}

        def dfs(i,cur):
            if (i,cur) in dp:
                return dp[(i,cur)]
            if cur == amount: return 1
            if cur > amount:
                return 0
            ways = 0
            for i in range(i,n):
                ways += dfs(i,cur+coins[i])
            dp[(i,cur)] = ways
            return ways

        return dfs(0,0)
            

