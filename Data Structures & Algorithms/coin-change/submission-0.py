class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = 0
        for num in reversed(coins):
            while amount - num >= 0:
                count += 1
                amount -= num

        return count if amount == 0 else -1