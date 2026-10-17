class Solution:
    def climbStairs(self, n: int) -> int:
        one_prev,two_prev = 1,1

        for i in range(n):
            current = one_prev + two_prev
            one_prev,two_prev = two_prev, current

        return one_prev

