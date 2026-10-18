class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+1)
        if amount == 0:
            return 0

        for i in range(1,amount+1):
            cur = i
            best = float('inf')
            for coin in coins:
                if cur - coin == 0:
                    best = 0
                if cur - coin > 0 and dp[cur-coin] != 0:
                    best = min(best,dp[cur-coin])
            dp[i] = best + 1 if best != float('inf') else 0
        print(dp)
        return -1 if dp[amount] == 0 else dp[amount] 
            